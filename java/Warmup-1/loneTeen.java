public boolean loneTeen(int a, int b) {
  boolean aT = (a >= 13 && a <= 19);
  boolean bT = (b >= 13 && b <= 19);
  return (aT && !bT) || (!aT && bT);
}
