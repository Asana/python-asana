module.exports = {
  resource: {
    template: 'resource.ejs',
    filename: function(resource, helpers) {
      return helpers.plural(resource.name) + '.py';
    }
  }
};
