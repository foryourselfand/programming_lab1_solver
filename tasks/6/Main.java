public class Main {
	public static void main(String[] args) {
		short[] h = {3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25};
		
		double[] x = new double[13];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 22.0 - 8.0;
				
		double[][] n = new double[12][13];
		for (int i = 0; i < n.length; i++) {
			for (int j = 0; j < n[i].length; j++) {
				switch (h[i]) {
					case 17:
						n[i][j] = ln(sin^2((1/3/(3/4+x)/x)^2));
						break;
					case 5:
					case 7:
					case 9:
					case 11:
					case 21:
					case 25:
						n[i][j] = (0.5*(root(3)(e^(x))+2/3))^(tan(1/4/(2/3-x)));
						break;
					default:
						n[i][j] = ((1/4+e^(((x)^(1/4/x)-2)^3))/4)^(tan((tan(x)*(1-arcsin((x+3)/22)))^(ln(abs(x)))));
						break;
				}
				System.out.printf("%.2f ", n[i][j]);
			}
			System.out.println();
		}
	}
}
