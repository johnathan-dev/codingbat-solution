public String startOz(String str) {
  String newString = "";
  if(str.equals("o") || str.equals("z") || str.length() < 2) return str;
  if(str.substring(0, 1).equals("o")) newString += "o";
  if(str.substring(1, 2).equals("z")) newString += "z";
  return newString;
}
