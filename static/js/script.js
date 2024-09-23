document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.menu-item');
    const menuContents = document.querySelectorAll('.menu-content');

    menuItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const target = this.getAttribute('data-target');

            // Hide all menu contents
            menuContents.forEach(content => {
                content.classList.add('d-none');
            });

            // Show the selected menu content
            document.getElementById(target).classList.remove('d-none');

            // Remove active class from all items
            menuItems.forEach(menuItem => {
                menuItem.classList.remove('active');
            });

            // Add active class to clicked item
            this.classList.add('active');
        });
    });
});