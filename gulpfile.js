var gulp = require('gulp');
var browserify = require('browserify');
var tsify = require('tsify');
var source = require('vinyl-source-buffer');

gulp.task('build', function () {
    browserify()
        .add('src/ts/index.ts')
        .plugin(tsify, { noImplicitAny: true })
        .bundle()
        .on('error', console.error.bind(console))
        .pipe(source('bundle.js'))
        .pipe(gulp.dest('dist'));
});
