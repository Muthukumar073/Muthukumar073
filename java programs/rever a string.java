public class Main{
    public static void main(String[] args){
        String name="muthukumar";
        String rev_name="";
        System.out.println("The Original name :"+name);
        for(int i=0;i<name.length();i++){
           rev_name=name.charAt(i)+rev_name;
        }
        System.out.println("The Reversed name :"+rev_name);
        }
    }
