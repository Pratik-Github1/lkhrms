$(function () {
    // Basic DataTable
    $("#basic-datatable").DataTable({
        language: {
            searchPlaceholder: "Search...",
            sSearch: ""
        }
    });

    // Responsive DataTable
    $("#responsive-datatable").DataTable({
        scrollX: "100%",
        language: {
            searchPlaceholder: "Search...",
            sSearch: ""
        }
    });

    // File DataTable with export buttons
    var fileDataTable = $("#file-datatable").DataTable({
        buttons: [
            {
                extend: 'pdfHtml5',
                title: window.location.pathname.split('/').pop(), // Use the last part of the URL as the title
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'excelHtml5',
                title: window.location.pathname.split('/').pop(),
                exportOptions: {
                    columns: ':visible'
                }
            },
            // Other buttons...
        ],
        scrollX: "100%",
        language: {
            searchPlaceholder: "Search...",
            sSearch: ""
        }
    });

    // Move the export buttons container to the desired location in the layout
    fileDataTable.buttons().container().appendTo("#file-datatable_wrapper .col-md-6:eq(0)");

    // Delete DataTable
    var deleteDataTable = $("#delete-datatable").DataTable({
        language: {
            searchPlaceholder: "Search...",
            sSearch: ""
        }
    });

    // Handle row selection in deleteDataTable
    $("#delete-datatable tbody").on("click", "tr", function () {
        $(this).hasClass("selected") ?
            $(this).removeClass("selected") :
            (deleteDataTable.$("tr.selected").removeClass("selected"),
            $(this).addClass("selected"));
    });

    // Handle button click to delete selected row
    $("#button").click(function () {
        deleteDataTable.row(".selected").remove().draw(false);
    });

    // Initialize Select2
    $(".select2").select2({
        minimumResultsForSearch: Infinity
    });
});
