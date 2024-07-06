import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

public class FormPesananRestoranIbraNuryaman extends JFrame {
    private JTextField nomorMejaField;
    private JComboBox<String> paket1ComboBox, paket2ComboBox, paket3ComboBox;
    private JTextField harga1Field, harga2Field, harga3Field;
    private JTextField jumlahBeli1Field, jumlahBeli2Field, jumlahBeli3Field;
    private JTextField bayar1Field, bayar2Field, bayar3Field;
    private JTextField totalPesananField;
    private JButton tombolBayar;

    public FormPesananRestoranIbraNuryaman() {
        setTitle("Form Pesanan Restoran - Ibra Nuryaman");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.insets = new Insets(5, 5, 5, 5);

        // Nomor meja
        gbc.gridx = 0;
        gbc.gridy = 0;
        panel.add(new JLabel("No. Meja"), gbc);
        
        gbc.gridx = 1;
        gbc.gridy = 0;
        nomorMejaField = new JTextField(10);
        panel.add(nomorMejaField, gbc);

        // Headers
        gbc.gridx = 0;
        gbc.gridy = 1;
        panel.add(new JLabel("Ket. Paket"), gbc);
        
        gbc.gridx = 1;
        gbc.gridy = 1;
        panel.add(new JLabel("Harga"), gbc);
        
        gbc.gridx = 2;
        gbc.gridy = 1;
        panel.add(new JLabel("Jml. Beli"), gbc);
        
        gbc.gridx = 3;
        gbc.gridy = 1;
        panel.add(new JLabel("Bayar"), gbc);

        // Baris 1
        gbc.gridx = 0;
        gbc.gridy = 2;
        paket1ComboBox = new JComboBox<>(new String[] {"Nasi Putih", "Nasi Goreng", "Mie Goreng"});
        panel.add(paket1ComboBox, gbc);
        
        gbc.gridx = 1;
        gbc.gridy = 2;
        harga1Field = new JTextField(10);
        panel.add(harga1Field, gbc);
        
        gbc.gridx = 2;
        gbc.gridy = 2;
        jumlahBeli1Field = new JTextField(10);
        panel.add(jumlahBeli1Field, gbc);
        
        gbc.gridx = 3;
        gbc.gridy = 2;
        bayar1Field = new JTextField(10);
        bayar1Field.setEditable(false);
        panel.add(bayar1Field, gbc);

        // Baris 2
        gbc.gridx = 0;
        gbc.gridy = 3;
        paket2ComboBox = new JComboBox<>(new String[] {"Ayam Penyet", "Sate Ayam", "Soto Ayam"});
        panel.add(paket2ComboBox, gbc);
        
        gbc.gridx = 1;
        gbc.gridy = 3;
        harga2Field = new JTextField(10);
        panel.add(harga2Field, gbc);
        
        gbc.gridx = 2;
        gbc.gridy = 3;
        jumlahBeli2Field = new JTextField(10);
        panel.add(jumlahBeli2Field, gbc);
        
        gbc.gridx = 3;
        gbc.gridy = 3;
        bayar2Field = new JTextField(10);
        bayar2Field.setEditable(false);
        panel.add(bayar2Field, gbc);

        // Baris 3
        gbc.gridx = 0;
        gbc.gridy = 4;
        paket3ComboBox = new JComboBox<>(new String[] {"Aqua", "Teh Botol", "Jus Jeruk"});
        panel.add(paket3ComboBox, gbc);
        
        gbc.gridx = 1;
        gbc.gridy = 4;
        harga3Field = new JTextField(10);
        panel.add(harga3Field, gbc);
        
        gbc.gridx = 2;
        gbc.gridy = 4;
        jumlahBeli3Field = new JTextField(10);
        panel.add(jumlahBeli3Field, gbc);
        
        gbc.gridx = 3;
        gbc.gridy = 4;
        bayar3Field = new JTextField(10);
        bayar3Field.setEditable(false);
        panel.add(bayar3Field, gbc);

        // Total Pesanan
        gbc.gridx = 0;
        gbc.gridy = 5;
        panel.add(new JLabel("Total Pesanan"), gbc);
        
        gbc.gridx = 1;
        gbc.gridy = 5;
        totalPesananField = new JTextField(10);
        totalPesananField.setEditable(false);
        panel.add(totalPesananField, gbc);

        // Tombol Bayar
        gbc.gridx = 2;
        gbc.gridy = 5;
        gbc.gridwidth = 2;
        tombolBayar = new JButton("Bayar");
        panel.add(tombolBayar, gbc);
        
        // Tambahkan panel ke frame
        add(panel);

        // Item listeners untuk paket combo boxes
        paket1ComboBox.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                updateHarga1();
            }
        });

        paket2ComboBox.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                updateHarga2();
            }
        });

        paket3ComboBox.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                updateHarga3();
            }
        });

        // Action listener untuk tombol bayar
        tombolBayar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                hitungTotalPesanan();
            }
        });

        setVisible(true);
    }

    private void updateHarga1() {
        switch ((String) paket1ComboBox.getSelectedItem()) {
            case "Nasi Putih":
                harga1Field.setText("10000");
                break;
            case "Nasi Goreng":
                harga1Field.setText("15000");
                break;
            case "Mie Goreng":
                harga1Field.setText("12000");
                break;
        }
    }

    private void updateHarga2() {
        switch ((String) paket2ComboBox.getSelectedItem()) {
            case "Ayam Penyet":
                harga2Field.setText("20000");
                break;
            case "Sate Ayam":
                harga2Field.setText("18000");
                break;
            case "Soto Ayam":
                harga2Field.setText("17000");
                break;
        }
    }

    private void updateHarga3() {
        switch ((String) paket3ComboBox.getSelectedItem()) {
            case "Aqua":
                harga3Field.setText("3000");
                break;
            case "Teh Botol":
                harga3Field.setText("5000");
                break;
            case "Jus Jeruk":
                harga3Field.setText("8000");
                break;
        }
    }

    private void hitungTotalPesanan() {
        try {
            int harga1 = Integer.parseInt(harga1Field.getText());
            int harga2 = Integer.parseInt(harga2Field.getText());
            int harga3 = Integer.parseInt(harga3Field.getText());

            int jumlahBeli1 = Integer.parseInt(jumlahBeli1Field.getText());
            int jumlahBeli2 = Integer.parseInt(jumlahBeli2Field.getText());
            int jumlahBeli3 = Integer.parseInt(jumlahBeli3Field.getText());

            int bayar1 = harga1 * jumlahBeli1;
            int bayar2 = harga2 * jumlahBeli2;
            int bayar3 = harga3 * jumlahBeli3;

            bayar1Field.setText(String.valueOf(bayar1));
            bayar2Field.setText(String.valueOf(bayar2));
            bayar3Field.setText(String.valueOf(bayar3));

            int total = bayar1 + bayar2 + bayar3;
            totalPesananField.setText(String.valueOf(total));
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Mohon masukkan angka yang valid.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        new FormPesananRestoranIbraNuryaman();
    }
}