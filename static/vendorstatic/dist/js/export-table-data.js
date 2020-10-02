/*Export Table Init*/

"use strict"; 

$(document).ready(function() {
	$('#example, #datatable1, .datatables').DataTable( {
        // "pagingType": "full_numbers",
		"lengthMenu": [
            [25, 50, 100, -1],
            [25, 50, 100, "All"]
        ],
		dom: 'Blfrtip',
		buttons: [
			'copy', 'csv', 'excel', 'pdf', 'print'
		]
		// responsive: false,
        // language: {
        //   search: "_INPUT_",
        //   searchPlaceholder: "Search records",
        // }
	} );
} );