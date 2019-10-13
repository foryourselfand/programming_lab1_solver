public class Main {
	public static void main(String[] args) {
		short[] h = {3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25};
		
		double[] x = new double[13];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 22.0 - 8.0;
				
		double[][] n = new double[12][13];
		for (int i = 0; i < n.length; i++) {
			for (int j = 0; j < n[i].length; j++) {
				switch ((int) h[i]) {
					case 17:
						n[i][j] = Math.log(Math.pow(Math.sin(Math.pow((1/3/(3/4+x[j])/x[j]), 2)), 2));
						break;
					case 5:
					case 7:
					case 9:
					case 11:
					case 21:
					case 25:
						n[i][j] = Math.pow((0.5*(Math.cbrt(Math.pow(Math.E, (x[j])))+2/3)), (Math.tan(1/4/(2/3-x[j]))));
						break;
					default:
						n[i][j] = Math.pow(((Math.pow(1/4+Math.E, (Math.pow((Math.pow((x[j]), (1/4/x[j]))-2), 3))))/4), (Math.tan(Math.pow((Math.tan(x[j])*(1-Math.asin((x[j]+3)/22))), (Math.log(Math.abs(x[j])))))));
						break;
				}
				System.out.printf("%.2f ", n[i][j]);
			}
			System.out.println();
		}
	}
}
