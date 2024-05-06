public class hanoi {

    public static void towerofHanoi(int n, tower source, tower dest, tower aux){
        if (n==1){
            int disk = source.popDisk();
            dest.pushDisk(disk);
            System.out.println("Move disk " + disk + "from " + source.getName()+ "to " + dest.getName());
            printTowers(source,dest,aux);
            return;
        }

        towerofHanoi(n-1,source,aux,dest);
        int disk = source.popDisk();
        dest.pushDisk(disk);
        System.out.println("Move disk " + disk + " from " + source.getName()+ "to " + dest.getName());
        printTowers(source,dest,aux);
        towerofHanoi(n-1, aux,dest,source);

    }

    public static void printTowers(tower source, tower dest, tower aux){
        source.print();
        aux.print();
        dest.print();
        System.out.println("-------");
    }

}

