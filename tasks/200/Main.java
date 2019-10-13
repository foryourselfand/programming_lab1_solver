public class Main {
	public static void main(String[] args) {
		int[] d = {6, 8, 10, 12, 14, 16, 18, 20, 22, 24};
		
		float[] x = new float[17];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 17.0 - 15.0);
				
		double[][] c = new double[10][17];
		for (int i = 0; i < c.length; i++) {
			for (int j = 0; j < c[i].length; j++) {
				switch ((int) d[i]) {
					case 8:
						c[i][j] = Math.pow((Math.asin(Math.pow(Math.E, (-Math.abs(x[j]))))), ((Math.tan(Math.pow(Math.E, (x[j])))+1)/4));
						break;
					case 6:
					case 12:
					case 14:
					case 16:
					case 22:
						c[i][j] = Math.sin(Math.pow((1/2/(Math.pow((1/2/x[j]), (x[j]))-1)), (Math.sin(x[j]))));
						break;
					default:
						c[i][j] = Math.pow((1/2*Math.pow((Math.asin((x[j]-6.5)/17)), 2/)(1/4-Math.tan(Math.tan(Math.pow((x[j]/2), 2))))), 2);
						break;
				}
				System.out.printf("%.2f ", c[i][j]);
			}
			System.out.println();
		}
	}
}
