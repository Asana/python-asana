package com.asana.codegen;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.apache.commons.lang3.StringUtils;

import io.swagger.codegen.v3.*;
import io.swagger.codegen.v3.generators.python.*;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.media.Schema;

public class PythonClientCodegenGenerator extends PythonClientCodegen {
    public PythonClientCodegenGenerator() {
        super();
        // Let the generator know about our code samples template so it can generate examples for our developer docs
        apiDocTemplateFiles.put("code_samples.mustache", ".yaml");

        // Remove model template files so that the generator does not generate models
        modelTemplateFiles.remove("model.mustache");
        modelTestTemplateFiles.remove("model_test.mustache");
        modelDocTemplateFiles.remove("model_doc.mustache");
    }

    @Override
    public void processOpts() {
        // Custom generators do not set the CodegenConstants
        additionalProperties.put(CodegenConstants.PACKAGE_NAME, "asana");
        setPackageName("asana");

        additionalProperties.put(CodegenConstants.PROJECT_NAME, "asana");
        setProjectName("asana");

        super.processOpts();

        // Remove <packageName>/models folder and <packageName>/models/__init__.py file from generation
        final String packageFolder = packageName.replace('.', File.separatorChar);
        supportingFiles.remove(new SupportingFile("__init__model.mustache", packageFolder + File.separatorChar + "models", "__init__.py"));

        // Create a definition for collection to be used in pagination
        supportingFiles.add(new SupportingFile("__init__pagination.mustache", packageFolder + File.separatorChar + "pagination", "__init__.py"));
        supportingFiles.add(new SupportingFile("page_iterator.mustache", packageFolder + File.separatorChar + "pagination", "page_iterator.py"));
        supportingFiles.add(new SupportingFile("event_iterator.mustache", packageFolder + File.separatorChar + "pagination", "event_iterator.py"));
    }

    @Override
    public String toVarName(String name) {
        // Return the name as defined in the OAS rather than formatting it. EX: instead of returning modified_on_after -> modified_on.after
        return name;
    }

    @Override
    public void setParameterExampleValue(CodegenParameter p) {
        // Our example correction code must execute before super, to ensure that
        // super does its special magic of determining the example type:
        // https://github.com/swagger-api/swagger-codegen-generators/blob/master/src/main/java/io/swagger/codegen/v3/generators/python/PythonClientCodegen.java#L639
        ExampleUtility.tryToSetExample(p);

        String example;
        if (p.defaultValue == null) {
            example = p.example;
        } else {
            example = p.defaultValue;
        }

        String type = p.baseType;
        if (type == null) {
            type = p.dataType;
        }

        if ("String".equals(type) || "str".equalsIgnoreCase(type)) {
            if (example == null) {
                example = p.paramName + "_example";
            }
            // Change opt_fields example from ["param1", "param2"] -> "param1,param2"
            String cleanedInput = example.replace("[", "").replace("]", "").replace("\"", "");
            String[] fields = cleanedInput.split(",");
            String exampleOptFieldString = String.join(",", fields);
            p.example = "\"" + exampleOptFieldString + "\"";
            return;
        } else if ("BOOLEAN".equalsIgnoreCase(type) || "bool".equalsIgnoreCase(type)) {
            // Fix boolean example showing wrong python boolean type EX: "false" instead of "False"
            // p.example is a string "true" or "false". We'll need to capitalize the first letter so that the sample code in python show True or False value
            p.example = p.example.substring(0, 1).toUpperCase() + p.example.substring(1);
           return;
        }

        // Update example value for requests that require a request body
        if (!languageSpecificPrimitives.contains(type)) {
            // Type is a model class, e.g. User
            p.example = "{\"data\": {\"<PARAM_1>\": \"<VALUE_1>\", \"<PARAM_2>\": \"<VALUE_2>\",}}";
            p.dataType = "dict";
            return;
        }

        super.setParameterExampleValue(p);
    }

    @Override
    public CodegenOperation fromOperation(String path, String httpMethod, Operation operation, Map<String, Schema> schemas, OpenAPI openAPI) {
        CodegenOperation op = super.fromOperation(path, httpMethod, operation, schemas, openAPI);
        // Set vendor-extension to be used in code_sample.mustache template to show how to use custom field query param in examples:
        if(op.operationId.equalsIgnoreCase("search_tasks_for_workspace")) {
            op.vendorExtensions.put("x-codegen-isSearchTasksForWorkspace", true);
        }

        // Set vendor-extension to be used in api.mustache to import the event iterator if the endpoint is the /events endpoint
        op.vendorExtensions.put("x-codegen-isGetEvents", op.operationId.equalsIgnoreCase("get_events"));

        // Convert operatioId from snake case to lower case string with no underscores. EX: get_custom_field_settings_for_project -> getcustomfieldsettingsforproject
        // This will be used to build the link to link to the developer documentation for that particular operation
        op.vendorExtensions.put("x-codegen-operationIdLowerCase", op.operationId.replace("_", "").toLowerCase());

        // Check if the returnType has "Array" in the name EX: TaskResponseArray
        // This will be used to check if an endpoint should return a collection object or not
        op.vendorExtensions.put("x-codegen-isArrayResponse", op.returnType.contains("Array"));

        // Generate resource instance variable name from the tag. EX: custom_field_settings -> custom_field_settings_api_instance
        String resourceInstanceName = generateResourceInstanceName(operation.getTags().get(0));
        op.vendorExtensions.put("x-codegen-resourceInstanceName", resourceInstanceName);

        // Fix PUT endpoints not adding comma in method request for sample docs. EX: .update_task(bodytask_gid, opts) -> .update_task(body, task_gid, opts)
        // Make a copy of parameters to be used in the template (templateParams). This is a hacky work around. We noticed that the below code "p.vendorExtensions.put"
        // does not update the parameter's vendorExtensions for POST and PUT endpoints so to work around this we created a new list that does have those
        // vendorExtensions added
        List<CodegenParameter> templateParams = new ArrayList<CodegenParameter>();
        CodegenParameter lastRequired = null;
        CodegenParameter lastOptional = null;
        for (CodegenParameter p : op.allParams) {
            if (p.required) {
                lastRequired = p;
            } else {
                lastOptional = p;
            }
        }

        // Set vendor-extension to be used in template:
        //     x-codegen-hasMoreRequired
        //     x-codegen-hasMoreOptional
        //     x-codegen-hasRequiredParams
        for (CodegenParameter p : op.allParams) {
            if (p == lastRequired) {
                p.vendorExtensions.put("x-codegen-hasMoreRequired", false);
            } else if (p == lastOptional) {
                p.vendorExtensions.put("x-codegen-hasMoreOptional", false);
            } else {
                p.vendorExtensions.put("x-codegen-hasMoreRequired", true);
                p.vendorExtensions.put("x-codegen-hasMoreOptional", true);
            }
            templateParams.add(p.copy());
        }
        op.vendorExtensions.put("x-codegen-hasRequiredParams", lastRequired != null);
        op.vendorExtensions.put("x-codegen-templateParams",templateParams);

        return op;
    }

    static String generateResourceInstanceName(String inputString) {
        String snakeCaseString = inputString.replaceAll("\\s+", "_").toLowerCase();

        // Add "ApiInstance" to the end of the string
        return snakeCaseString.toString() + "_api_instance";
    }

    @SuppressWarnings("unchecked")
    @Override
    public Map<String, Object> postProcessOperations(Map<String, Object> objs) {
        // Generate and store argument list string of each operation into
        // vendor-extension: x-codegen-arg-list.
        Map<String, Object> operations = (Map<String, Object>) objs.get("operations");
        if (operations != null) {
            List<CodegenOperation> ops = (List<CodegenOperation>) operations.get("operation");
            for (CodegenOperation operation : ops) {
                List<String> argList = new ArrayList<String>();
                boolean hasOptionalParams = false;
                for (CodegenParameter p : operation.allParams) {
                    if (p.required) {
                        argList.add(p.paramName);
                    } else {
                        hasOptionalParams = true;
                    }
                }
                if (hasOptionalParams) {
                    argList.add("opts");
                }
                operation.vendorExtensions.put("x-codegen-arg-list", StringUtils.join(argList, ", "));
            }
        }
        return objs;
    }
}
