$(function () {
        $('#data').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                data: {'action': 'searchdata'},
                dataSrc: ""
            },
            columns: [
                {"data": "id"},
                {"data": "archivo"},
                {"data": "activo"},
                {"data": "opciones"},
            ],
            columnDefs: [
                {
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row){
                        var buttons = '<a href="/activos/vulnerabilidad/eliminar/'+row.id+'/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>';
                        return buttons;
                    }
                },
                {
                    targets: [1],
                    orderable: false,
                    render: function (data, type, row){
                        if (row.archivo != ""){
                            var archivo = '<a href="'+row.archivo+'" download="'+row.id+'">'+row.id+'</a>';
                            return archivo;
                        }else{
                            return "No disponible";
                        }

                    }
                }
            ],
            initComplete: function (settings, json){
            }
        });
});