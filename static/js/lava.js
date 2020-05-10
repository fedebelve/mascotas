
$("#buscarCliente").click(function () {
     console.log('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa');
      var cliente_nrodocumento = $("#inputCliente").val();

      $.ajax({
        url: '/ajax/validate_cliente/',
        data: {
          'cliente_nrodocumento': cliente_nrodocumento
        },
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
            alert("A user with this username already exists.");
          }
        }
      });

    });
