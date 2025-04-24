document.addEventListener("DOMContentLoaded", function () {
    const tableField = document.querySelector('#id_table');
    const dateField = document.querySelector('#id_reservation_date');
    const timeField = document.querySelector('#id_reservation_time');

    function fetchAvailableTimes() {
        const tableId = tableField.value;
        const date = dateField.value;

        if (!tableId || !date) return;

        fetch(`/get-available-times/?table_id=${tableId}&reservation_date=${date}`)
            .then(response => response.json())
            .then(data => {
                timeField.innerHTML = ''; // Clear old options

                if (data.times.length > 0) {
                    data.times.forEach(time => {
                        const option = document.createElement('option');
                        option.value = time;
                        option.textContent = time;
                        timeField.appendChild(option);
                    });
                } else {
                    const option = document.createElement('option');
                    option.textContent = 'No available time slots';
                    option.disabled = true;
                    timeField.appendChild(option);
                }
            });
    }

    tableField.addEventListener('change', fetchAvailableTimes);
    dateField.addEventListener('change', fetchAvailableTimes);
});