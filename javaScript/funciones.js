var operando1;
var operando2;
var operacion;

function cal() {
	var resultado = document.getElementById('resultado');
	var reset = document.getElementById('reset');
	var igual = document.getElementById('igual');
	var sum = document.getElementById('sum');
	var res = document.getElementById('res');
	var mult = document.getElementById('mult');
	var div = document.getElementById('div');
	var cero = document.getElementById('cero');
	var uno = document.getElementById('uno');
	var dos = document.getElementById('dos');
	var tres = document.getElementById('tres');
	var cuatro = document.getElementById('cuatro');
	var cinco = document.getElementById('cinco');
	var seis = document.getElementById('seis');
	var siete = document.getElementById('siete');
	var ocho = document.getElementById('ocho');
	var nueve = document.getElementById('nueve');

	cero.onclick = function(e) {
		resultado.textContent = resultado.textContent + '0';
	}
	uno.onclick = function(e) {
		resultado.textContent = resultado.textContent + '1';
	}
	dos.onclick = function(e) {
		resultado.textContent = resultado.textContent + '2';
	}
	tres.onclick = function(e) {
		resultado.textContent = resultado.textContent + '3';
	}
	cuatro.onclick = function(e) {
		resultado.textContent = resultado.textContent + '4';
	}
	cinco.onclick = function(e) {
		resultado.textContent = resultado.textContent + '5';
	}
	seis.onclick = function(e) {
		resultado.textContent = resultado.textContent + '6';
	}
	siete.onclick = function(e) {
		resultado.textContent = resultado.textContent + '7';
	}
	ocho.onclick = function(e) {
		resultado.textContent = resultado.textContent + '8';
	}
	nueve.onclick = function(e) {
		resultado.textContent = resultado.textContent + '9';
	}
	reset.onclick = function(e) {
		resetear();
	}
	sum.onclick = function(e) {
		operando1 = resultado.textContent;
		operacion = '+';
		limpiar();
	}
	res.onclick = function(e) {
		operando1 = resultado.textContent;
		operacion = '-';
		limpiar();
	}
	mult.onclick = function(e) {
		operando1 = resultado.textContent;
		operacion = '*';
		limpiar();
	}
	div.onclick = function(e) {
		operando1 = resultado.textContent;
		operacion = '/';
		limpiar();
	}
	igual.onclick = function(e) {
		operando2 = resultado.textContent;
		resolver();
	}

}

function limpiar() {
	resultado.textContent = "";
}

function resetear() {
	resultado.textContent = "";
	operando1 = 0;
	operando2 = 0;
	operacion = "";
}
function resolver() {
	var res = 0;
	switch(operacion) {
		case '+':
			res = parseFloat(operando1) + parseFloat(operando2);
		break;

		case '-':
			res = parseFloat(operando1) - parseFloat(operando2);
		break;

		case '*':
			res = parseFloat(operando1) * parseFloat(operando2);
		break;

		case '/':
			res = parseFloat(operando1) / parseFloat(operando2);
		break;
	}
	resetear();
	resultado.textContent = res;
}