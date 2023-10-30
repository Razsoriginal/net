import javax.crypto.Mac; 
import javax.crypto.spec.SecretKeySpec; 
import java.security.NoSuchAlgorithmException; 
import java.security.InvalidKeyException; 
import java.util.Base64; 
 
public class hmac { 
    public static void main(String[] args) { 
        String message = "Hello, HMAC!"; 
        String secretKey = "MySecretKey";  
 
        try { 
            SecretKeySpec secretKeySpec = new SecretKeySpec(secretKey.getBytes(), "HmacSHA512"); 
 
            Mac mac = Mac.getInstance("HmacSHA512"); 
 
            mac.init(secretKeySpec); 
 
            byte[] hmacBytes = mac.doFinal(message.getBytes()); 

            String hmacBase64 = Base64.getEncoder().encodeToString(hmacBytes); 
 
            System.out.println("HMAC (Base64): " + hmacBase64); 
 
        } catch (NoSuchAlgorithmException e) { 
            System.err.println("HMAC algorithm not available."); 
        } catch (InvalidKeyException e) { 
            System.err.println("Invalid secret key."); 
        } 
    } 
}