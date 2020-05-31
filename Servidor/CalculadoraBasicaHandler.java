import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import org.apache.thrift.TException;

public class CalculadoraBasicaHandler implements CalculadoraBasica.Iface {

    @Override
    public int Sumar(int numeroA, int numeroB) throws TException {
        return numeroA + numeroB;
    }

    @Override
    public int Restar(int numeroA, int numeroB) throws TException {
        return numeroA - numeroB;
    }

    @Override
    public int Multiplicar(int numeroA, int numeroB) throws TException {
        return numeroA * numeroB;
    }

    @Override
    public int Dividir(int numeroA, int numeroB) throws TException {
        if (numeroB == 0){
            return -1;
        }
        int modulo = numeroA % numeroB;
        return (numeroA - modulo) / numeroB;
    }
}
