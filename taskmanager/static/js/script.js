document.addEventListener('DOMContentLoaded', function() {

    // Sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Datepicker initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmm, yyyy",
        i18n: {done: "Select"}
    });
  });

