public boolean parrotTrouble(boolean talking, int hour) {
  return (((hour < 7) || (hour > 20)) && talking);
}
