package main

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"log"
	"net"
	"net/http"
	"net/rpc"
	"net/rpc/jsonrpc"
	"rpcTest/server"
)

func rpcClient() {
	client, err := rpc.Dial("tcp", "localhost:1234")
	if err != nil {
		log.Fatal("dialing: ", err)
	}
	args := server.Args{A: 1, B: 3}
	var reply int
	err = client.Call("MathServer.Add", args, &reply)
	if err != nil {
		log.Fatal("calling MathServer.Add: ", err)
	}
	fmt.Printf("MathServer.Add: %d+%d=%d", args.A, args.B, reply)
}

func httpRpcClient() {
	client, err := rpc.DialHTTP("tcp", "localhost:1234")
	if err != nil {
		log.Fatal("dialing: ", err)
	}
	args := server.Args{A: 1, B: 3}
	var reply int
	err = client.Call("MathServer.Add", args, &reply)
	if err != nil {
		log.Fatal("calling MathServer.Add: ", err)
	}
	fmt.Printf("MathServer.Add: %d+%d=%d", args.A, args.B, reply)
}

func jsonRpcClient() {
	client, err := jsonrpc.Dial("tcp", "localhost:1234")
	if err != nil {
		log.Fatal("dialing: ", err)
	}
	args := server.Args{A: 1, B: 3}
	var reply int
	err = client.Call("MathServer.Add", args, &reply)
	if err != nil {
		log.Fatal("calling MathServer.Add: ", err)
	}
	fmt.Printf("MathServer.Add: %d+%d=%d", args.A, args.B, reply)
}

func DialHTTP(network, address string) (*rpc.Client, error) {
	return DialHTTPPATH(network, address, rpc.DefaultRPCPath)
}

func DialHTTPPATH(network, address string, path string) (*rpc.Client, error) {
	var err error
	conn, err := net.Dial(network, address)
	if err != nil {
		return nil, err
	}
	io.WriteString(conn, "GET "+path+" HTTP/1.0\n\n")
	resp, err := http.ReadResponse(bufio.NewReader(conn), &http.Request{Method: "GET"})
	connected := "200 ltj"
	if err == nil && resp.Status == connected {
		return jsonrpc.NewClient(conn), nil
	}
	if err == nil {
		err = errors.New("unexpected HTTP response: " + string(resp.Status))
	}

	conn.Close()
	return nil, &net.OpError{Op: "dail-http", Net: network + " " + address, Addr: nil, Err: err}
}

func httpJsonRpcClient(){
	client, err := DialHTTP("tcp", "localhost:1234")
	if err != nil {
		log.Fatal("dialing: ", err)
	}
	args := server.Args{A: 1, B: 3}
	var reply int
	err = client.Call("MathServer.Add", args, &reply)
	if err != nil {
		log.Fatal("calling MathServer.Add: ", err)
	}
	fmt.Printf("MathServer.Add: %d+%d=%d", args.A, args.B, reply)

}

func main() {
	// rpcClient()
	// httpRpcClient()
	// jsonRpcClient()
	httpJsonRpcClient()
}
