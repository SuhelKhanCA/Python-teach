# method overloading
# compile time polymorphism 

class Main{
    static int sum(int a, int b){
        return a + b;
    }
    static int sum(int a, int b, int c){
        return a + b + c;
    }
    public static void main(String[] args){
        System.out.println(sum(12, 12));
        System.out.println(sum(12, 10, 56));
    }
}