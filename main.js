// Tugas: Buat fungsi untuk mengurutkan array angka dari terkecil ke terbesar
// // Test case
// const students = [
//     { name: 'John', age: 25 },
//     { name: 'Jane', age: 20 },
//     { name: 'Bob', age: 22 }
// ];

// console.log(sortNumbers([5, 2, 9, 1, 7]));
// // Expected output: [1, 2, 5, 7, 9]
// console.log(students)
// console.log("after sorting")
// console.log(sortStudentsByAge(students))

// function getTopThreeEvenNumbers(arr) {
//     return arr.sort((a,b)  => b - a).filter(a => a % 2 === 0).slice(0,3)
//  }
 
//  // Test case
//  console.log(getTopThreeEvenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));
//  // Expected output: [10, 8, 6]
function sortNumbers(arr) {
    return arr.sort((a,b)  => a-b)
}
// Tugas: Urutkan array objek mahasiswa berdasarkan umur
function sortStudentsByAge(students) {
    return students.sort((a,b)  => a.age - b.age)
}
function cariAngkaYangSeringMuncul(arr) {
    const freq = {}

    arr.forEach(element => {
        freq[element]  = (freq[element] || 0) + 1
    });


    let angkaTerbanyak = [];
    let jumlahTertinggi = 0;
    console.log(freq)
    for (const [angka, jumlah] of Object.entries(freq)) {
        if (jumlah > jumlahTertinggi) {
            jumlahTertinggi = jumlah;
            angkaTerbanyak = [Number(angka)];
            console.log(angka,jumlah)
        } else if (jumlah === jumlahTertinggi) {
            angkaTerbanyak.push(Number(angka));
        }
    }
    return angkaTerbanyak;
}

// Test case
console.log(cariAngkaYangSeringMuncul([64, 34, 25, 12, 12,64,25,25,25,22, 11, 90]));



