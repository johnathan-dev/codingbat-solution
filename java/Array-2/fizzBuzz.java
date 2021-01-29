public String[] fizzBuzz(int start, int end) {
  String[] newArr = new String[end-start];
  String add;
  for(int i=0; i<newArr.length; i++){
    add = "";
    if(start % 3 == 0){
      add += "Fizz";
    }
    if(start % 5 == 0){
      add += "Buzz";
    }
    if(!(start % 3 == 0) && !(start % 5 == 0)){
      add = String.valueOf(start);
    }
    newArr[i] = add;
    start++;
  }
  return newArr;
}
