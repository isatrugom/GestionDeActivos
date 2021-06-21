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
                {"data": "nombre"},
                {"data": "impacto"},
                {"data": "timestamp"},
                {"data": "modelo"},
                {"data": "proveedor"},
                {"data": "numeroDeSerie"},
                {"data": "tipoHardware"},
                {"data": "redAsociada"},
                {"data": "tipoEquipo"},
                {"data": "opciones"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    render: function (data, type, row){
                        var nombre = '<a href="/activos/activo/vulnerabilidades/'+row.id+'/">'+row.nombre+'</a>';
                        return nombre
                    }
                },
                {
                    targets: [2],
                    render: function (data, type, row){
                        var fecha = row.timestamp.split('-')[2].split('T')[0] + "-" + row.timestamp.split('-')[1] + "-" + row.timestamp.split('-')[0];
                        var hora = row.timestamp.split('T')[1].substring(0, 5);
                        return fecha + " " + hora
                    }
                },
                {
                    targets: [9],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row){
                        var buttons = '<a href="/activos/equipoRed/editar/'+row.id+'/" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a>&nbsp';
                        buttons += '<a href="/activos/equipoRed/eliminar/'+row.id+'/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>&nbsp';
                        buttons += '<a href="#" type="button" class="btn btn-secondary btn-xs"><i class="fas fa-exclamation-triangle"></i></a>';
                        return buttons;
                    }
                }
            ],
            initComplete: function (settings, json){
            }
        });
});