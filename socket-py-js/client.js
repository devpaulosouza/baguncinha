const net = require('net');
const client = new net.Socket();

client.connect(8484, '127.0.0.1', () => {
    console.log('Conectado');
    client.write('Conectou cacete!');
});

client.on('data', (data) => {
    console.log('Mensagem recebida', data);
    client.destroy();
})