package com.asana.codegen;

import java.util.Map;

import org.json.*;
import io.swagger.codegen.v3.generators.python.*;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.media.Schema;
import io.swagger.codegen.v3.*;

public class PythonClientCodegenGenerator extends PythonClientCodegen {
  public PythonClientCodegenGenerator() {
    super();
    apiDocTemplateFiles.put("code_samples.mustache", ".yaml");
  }

  @Override
  public void processOpts() {
    // custom generators do not set the CodegenConstants
    additionalProperties.put(CodegenConstants.PACKAGE_NAME, "asana");
    setPackageName("asana");

    additionalProperties.put(CodegenConstants.PROJECT_NAME, "asana");
    setProjectName("asana");

    // Super must be called AFTER our modification, otherwise the package name
    // somehow ends up wrong
    super.processOpts();
  }

  @Override
  public void setParameterExampleValue(CodegenParameter p) {
    // Our example correction code must execute before super, to ensure that
    // super does its special magic of determining the example type:
    // https://github.com/swagger-api/swagger-codegen-generators/blob/master/src/main/java/io/swagger/codegen/v3/generators/python/PythonClientCodegen.java#L639
    ExampleUtility.tryToSetExample(p);

    // "CSV" is used to declare that a query param string is joined by commas.
    // If that's the case, we can use the raw JSON representation as a valid
    // python list as the syntax is the same
    if ("csv".equalsIgnoreCase(p.collectionFormat)) {
      return;
    }

    super.setParameterExampleValue(p);

    String type = p.baseType;
    if (type == null) {
      type = p.dataType;
    }

    // Update example for requests that require body
    if (!languageSpecificPrimitives.contains(type)) {
      // type is a model class, e.g. User
      String bodyData = "({\"param1\": \"value1\", \"param2\": \"value2\",})";
      p.example = this.packageName + "." + type + bodyData;
    }
  }

  @Override
  public CodegenOperation fromOperation(String path, String httpMethod, Operation operation, Map<String, Schema> schemas, OpenAPI openAPI) {
    CodegenOperation op = super.fromOperation(path, httpMethod, operation, schemas, openAPI);
    if(op.operationId.equalsIgnoreCase("search_tasks_for_workspace")) {
      op.vendorExtensions.put("x-codegen-isSearchTasksForWorkspace", true);
    }
    return op;
  }
}
