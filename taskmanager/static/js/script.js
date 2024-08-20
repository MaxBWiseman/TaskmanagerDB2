document.addEventListener("DOMContentLoaded", function() {
    // side nav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
    // modal initialization
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
    // datepicker initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: 'dd mmm, yyyy',
        i18n: {done: 'Select'}
    });
    // select initialization
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
    // tasks collapsible initialization
    let collapsible= document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible);
});

// JavaScript to dynamically set the current year
document.getElementById('current-year').textContent = new Date().getFullYear();