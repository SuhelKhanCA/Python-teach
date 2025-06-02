class Student{
    String name; int age; boolean isAdult;

    Student(String name, int age, boolean isAdult){
        this.name = name;
        this.age = age;
        this.isAdult = isAdult;
    }


    public static void main(String [] args){

        Student s1 = new Student("Suhel", 34, true);

        System.out.print(s1.name);

    }
}



// function constructor(){
//     this.name = name
// }