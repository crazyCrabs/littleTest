package main

import (
	"io"
	"log"
	"net"
	"net/http"
	"net/rpc"
	"net/rpc/jsonrpc"
	"rpcTest/server"
)

func rpcRpc() {
	rpc.RegisterName("MathServer", new(server.MathServer))
	l, e := net.Listen("tcp", ":1234")
	if e != nil {
		log.Fatal("listen error: ", e)
	}
	rpc.Accept(l)
}

func httpRpc() {
	rpc.RegisterName("MathServer", new(server.MathServer))
	l, e := net.Listen("tcp", ":1234")
	if e != nil {
		log.Fatal("listen error: ", e)
	}
	rpc.HandleHTTP()
	http.Serve(l, nil)
}

func jsonRpc() {
	rpc.RegisterName("MathServer", new(server.MathServer))
	l, e := net.Listen("tcp", ":1234")
	if e != nil {
		log.Fatal("listen error: ", e)
	}
	for {
		conn, err := l.Accept()
		if err != nil {
			log.Println("josnrpc.server: Accept:", err.Error())
			return
		}

		go jsonrpc.ServeConn(conn)
	}
}

func httpJsonRpc() {
	rpc.RegisterName("MathServer", new(server.MathServer))
	l, e := net.Listen("tcp", ":1234")
	if e != nil {
		log.Fatal("listen error: ", e.Error())
	}
	http.HandleFunc(rpc.DefaultRPCPath, func(rw http.ResponseWriter, r *http.Request) {
		conn, _, err := rw.(http.Hijacker).Hijack()
		if err != nil {
			log.Print("rpc hijacking ", r.RemoteAddr, ":", err.Error())
			return
		}

		var connected = "200 ltj"
		io.WriteString(conn, "HTTP/1.0 "+connected+"\n\n")
		jsonrpc.ServeConn(conn)
	})
	http.Serve(l, nil)
}

func main() {
	// rpcRpc() // rpc
	// httpRpc() // http rpc server
	// jsonRpc() // json rpc server
	httpJsonRpc()
}
