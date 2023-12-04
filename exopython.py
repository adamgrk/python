
def compute_imc(poids, taille):  # Do not touch
    # [START] Add your code here, replace the "0" with the necessary computation
    result = poids/taille**2
    result=round(result,2)
    # [END]
    return result  # Do not touch


if __name__ == "__main__":  # Do not touch
    # [START] Add your own tests here
    print(compute_imc(65, 1.70))
    print(compute_imc(60, 1.50))
    # [END]

