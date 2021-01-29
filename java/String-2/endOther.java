public boolean endOther(String a, String b) {
	if(a.length() < b.length()) {
		return b.substring(b.length()-a.length(), b.length()).toLowerCase().equals(a.toLowerCase());
	}
	return a.substring(a.length()-b.length(), a.length()).toLowerCase().equals(b.toLowerCase());
}
