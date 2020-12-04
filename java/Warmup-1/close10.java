public int close10(int a, int b) {
  int aClose = Math.abs(a - 10);
  int bClose = Math.abs(b - 10);
  if(aClose == bClose) return 0;
  if(aClose < bClose) return a;
  return b;
}
