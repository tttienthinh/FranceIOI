let read_int() = Scanf.scanf " %d" (fun x -> x)
let nbCartons = read_int()
let containers =
    Array.init (nbCartons + 1) (fun carton -> if carton = 0 then 0 else read_int());;

let tab = Array.make (-1) nbCartons;;
tab.(0) <- 0;

let rec trouver_produit recherche