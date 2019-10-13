public class Main {
	public static void main(String[] args) {
		short[] c = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
		
		double[] x = new double[14];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 14.0 - 12.0;
				
		double[][] f = new double[19][14];
		for (int i = 0; i < f.length; i++) {
			for (int j = 0; j < f[i].length; j++) {
				switch ((int) c[i]) {
					case 20:
						f[i][j] = Math.pow((Math.tan(Math.atan((x[j]-5)/14))), 2);
						break;
					case 2:
					case 5:
					case 8:
					case 10:
					case 11:
					case 12:
					case 13:
					case 14:
					case 18:
						f[i][j] = Math.sin(Math.cos(Math.pow((x[j]), (2*x[j]))));
						break;
					default:
						f[i][j] = Math.pow((Math.asin(Math.pow(Math.E, (Math.cbrt(-2*Math.abs(x[j])))))), (2*Math.pow((Math.pow((Math.tan(x[j])*(Math.log(Math.abs(x[j]))-2)), 3*)(Math.sin(Math.cbrt(x[j]))-1)), 2)));
						break;
				}
				System.out.printf("%.3f ", f[i][j]);
			}
			System.out.println();
		}
	}
}
