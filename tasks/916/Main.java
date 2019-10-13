public class Main {
	public static void main(String[] args) {
		short[] e = {2, 4, 6, 8, 10, 12, 14, 16};
		
		float[] x = new float[19];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 16.0 - 4.0);
				
		double[][] g = new double[8][19];
		for (int i = 0; i < g.length; i++) {
			for (int j = 0; j < g[i].length; j++) {
				switch ((int) e[i]) {
					case 2:
						g[i][j] = Math.pow(Math.E, (Math.tan(Math.pow(((x[j]+3/4)/x[j]), (x[j])))));
						break;
					case 4:
					case 8:
					case 12:
					case 16:
						g[i][j] = Math.cos(Math.log(Math.pow((3/Math.abs(x[j])), (x[j]))));
						break;
					default:
						g[i][j] = Math.tan(Math.sin(Math.log(4/Math.abs(x[j]))));
						break;
				}
				System.out.printf("%.5f ", g[i][j]);
			}
			System.out.println();
		}
	}
}
