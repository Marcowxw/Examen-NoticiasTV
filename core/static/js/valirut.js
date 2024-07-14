window.Parsley.addValidator('rut', {
	validateString: function(value) {
		value = value.replace('-', '-');
			if (!/^[0-9]+[-|-]{1}[0-9kK]{1}$/.test(value))
			return false;
			var tmp = value.split('-');
			var digv = tmp[1];
			var rut = tmp[0];

			if (digv == 'K') digv = 'k';
				return (dv(rut) == digv);
		},
		messages: {
			es: 'El RUT no es válido.'
		}
	});

	function dv(T) {
		var M=0,S=1;
		for(;T;T=Math.floor(T/10))
			S=(S+T%10*(9-M++%6))%11;
		return S ? S-1 : 'k';
	}
