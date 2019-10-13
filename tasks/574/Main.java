public class Main {
	public static void main(String[] args) {
		short[] h = {17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6};
		
		float[] x = new float[18];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 14.0 - 10.0);
				
		double[][] e = new double[12][18];
		for (int i = 0; i < e.length; i++) {
			for (int j = 0; j < e[i].length; j++) {
				switch ((int) h[i]) {
					case 16:
						e[i][j] = Math.atan(Math.pow(1/Math.E, (Math.abs(x[j]))));
						break;
					case 6:
					case 8:
					case 10:
					case 11:
					case 14:
					case 17:
						e[i][j] = Math.pow(Math.E, (Math.pow((Math.log(Math.abs(x[j]))), (2*(Math.asin((x[j]-3)/14)+1)))));
						break;
					default:
						e[i][j] = Math.pow((1-Math.pow((Math.cos(x[j]/(x[j]-1/4))), (Math.pow(Math.E, (Math.pow(Math.E, (x[j]))))/(Math.sin(Math.pow(Math.E, (x[j])))-0.25)))), 3);
						break;
				}
				System.out.printf("%.5f ", e[i][j]);
			}
			System.out.println();
		}
	}
}
