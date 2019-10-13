public class Main {
	public static void main(String[] args) {
		short[] d = {18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5};
		
		double[] x = new double[20];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 16.0 - 12.0;
				
		double[][] f = new double[14][20];
		for (int i = 0; i < f.length; i++) {
			for (int j = 0; j < f[i].length; j++) {
				switch (d[i]) {
					case 7:
						f[i][j] = arcsin(e^(root(3)(-sin^2(x))));
						break;
					case 5:
					case 6:
					case 8:
					case 9:
					case 15:
					case 16:
					case 17:
						f[i][j] = sin((3*(cos(x)-1))^((3*x)^3));
						break;
					default:
						f[i][j] = e^(e^(4*(1/2+x)))+1/2;
						break;
				}
				System.out.printf("%.3f ", f[i][j]);
			}
			System.out.println();
		}
	}
}
