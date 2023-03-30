import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        Socket clientSocket;
        BufferedReader in;
        PrintWriter out;
        Scanner sc=new Scanner(System.in);
        try{
            clientSocket =new Socket("localhost",5000);
            out=new PrintWriter(clientSocket.getOutputStream());
            in=new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

            Thread sender=new Thread(new Runnable() {
                String msg;
                @Override
                public void run() {
                    while(true){
                        msg=sc.nextLine();
                        out.println(msg);
                        out.flush();
                    }
                }
            });
            sender.start();
            Thread receiver=new Thread(new Runnable() {
                String msg;
                @Override
                public void run() {
                    try
                    {
                        msg=in.readLine();
                        while(msg!=null){
                            System.out.println("Server msg :"+msg);
                            msg=in.readLine();
                        }
                        System.out.println("Server not working");
                        out.close();
                        clientSocket.close();
                    } catch (Exception e) {
                        throw new RuntimeException(e);
                    }
                }
            });
            receiver.start();
        } catch (Exception e) {
           e.printStackTrace();
        }
    }
}
