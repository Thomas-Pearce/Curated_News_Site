var gulp        = require('gulp');
var browserSync = require('browser-sync').create();
var sass        = require('gulp-ruby-sass');

// Static Server + watching html files
gulp.task('serve', function() {
  console.log('hello world');
    browserSync.init({
        server: "./app"
    });
});

gulp.task('styles', function(){
  return sass('app/scss/*.scss')
  .pipe(gulp.dest('app/css'));
});


gulp.task('watch', function(){
  gulp.watch("app/*.html").on('change', browserSync.reload);
	gulp.watch("app/scss/*.scss", ['styles']);
  gulp.watch("app/css/*.css").on('change', browserSync.reload);
});

gulp.task('default', ['serve', 'watch']);