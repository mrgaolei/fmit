module.exports = function(grunt){
	var path = {
		webapp: 'app/'
	};
	grunt.initConfig({
		path: path,
		pkg: grunt.file.readJSON('package.json'),
		svgstore: {
			options: {
				includedemo: true
			},
			zu: {
				src: '<%= path.webapp %>/svg/source/*.svg',
				dest: '<%= path.webapp %>/svg/icons.svg'
			}
		}
	})

	grunt.loadNpmTasks('grunt-svgstore');

	grunt.registerTask('svg', [
		'svgstore:zu'
	]);
}