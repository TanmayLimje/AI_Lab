public class Main {
    public static void main(String[] args) {

        int n = 3;

        hanoi H = new hanoi();

        tower source = new tower('A');
        tower aux = new tower('B');
        tower dest = new tower('C');

        for (int i = n; i >= 1; i--){
            source.pushDisk(i);
        }

        System.out.println("Initial state:");
        hanoi.printTowers(source,aux,dest);

        System.out.println("Steps:");
        hanoi.towerofHanoi(n, source, aux, dest);
    }
}
