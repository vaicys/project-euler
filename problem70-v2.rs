fn euler_totient_sieve(limit: usize) -> Vec<usize> {
    let mut phi: Vec<usize> = (0..=limit).collect();
    for i in 2..=limit {
        if phi[i] == i {
            for j in (i..=limit).step_by(i) {
                phi[j] -= phi[j] / i;
            }
        }
    }

    phi
}

fn are_permutations(num1: usize, num2: usize) -> bool {
    let s1 = num1.to_string();
    let s2 = num2.to_string();

    if s1.len() != s2.len() {
        return false;
    }

    let mut chars1: Vec<char> = s1.chars().collect();
    let mut chars2: Vec<char> = s2.chars().collect();

    chars1.sort_unstable();
    chars2.sort_unstable();

    chars1 == chars2
}

fn main() {
    let limit = 10_000_000;
    let totient_values = euler_totient_sieve(limit);
    

    let mut min = f64::MAX;
    for i in 2..limit {
        if are_permutations(i, totient_values[i]) {
            let fraction = i as f64 / totient_values[i] as f64;
            if fraction < min {
                min = fraction;
                println!("{} {}", i, totient_values[i]);
            }
        }
    }
}
