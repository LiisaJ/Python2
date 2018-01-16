def kmh(arv_ms):
    arv_kmh = arv_ms * 60 * 60 / 1000
    return arv_kmh

kiirus_ms = 456

print("Kiirus on " + str(kiirus_ms) + " m/s.")
print("See on " + str(kmh(kiirus_ms)) + " km/h.")

      