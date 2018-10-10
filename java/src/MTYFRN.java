import java.util.*;
class Soolver {


    public static void main(String args[]) {


        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int a[]=new int[n];
            for(int i=0;i<n;i++){
                a[i]=sc.nextInt();
            }
            int v=0;
            if(n%2==0){
                v=n/2;
            }else{

                v=(n/2)+1;
            }
            int m[]=new int[v];
            int tomu[]=new int[n-v];

            for(int i=0;i<n;i++){
                if(i%2==0){
                    m[i/2]=a[i];
                }else{
                    tomu[(i/2)]=a[i];
                }
            }

            if(k>v-1){
                k=v-1;


                Arrays.sort(m);
                Arrays.sort(tomu);
                int motu[] = new int[v];
                for (int i = v - 1; i >= 0; i--) {
                    motu[v - i - 1] = m[i];
                }
                int pmotu = 0;
                int ptomu = 0;
                for (int i = 0; i < k; i++) {
                    pmotu += motu[i];
                    ptomu+=tomu[i];

                }
                int ttomu=0;
                int tmotu=0;
                for(int i=0;i<v;i++){
                    tmotu+=motu[i];
                }
                for(int i=0;i<n-v;i++){
                    ttomu+=tomu[i];
                }

                if((ttomu-ptomu+pmotu)>(tmotu-pmotu+ptomu)){
                    System.out.println("YES");
                }else{
                    System.out.println("NO");
                }



            }else {
                Arrays.sort(m);
                Arrays.sort(tomu);
                int motu[] = new int[v];
                for (int i = v - 1; i >= 0; i--) {
                    motu[v - i - 1] = m[i];
                }
                int pmotu = 0;
                int ptomu = 0;
                for (int i = 0; i < k; i++) {
                    pmotu += motu[i];
                    ptomu+=tomu[i];

                }
                int ttomu=0;
                int tmotu=0;
                for(int i=0;i<v;i++){
                    tmotu+=motu[i];
                }
                for(int i=0;i<n-v;i++){
                    ttomu+=tomu[i];
                }

                if((ttomu-ptomu+pmotu)>(tmotu-pmotu+ptomu)){
                    System.out.println("YES");
                }else{
                    System.out.println("NO");
                }

            }
        }
    }
}