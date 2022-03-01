# Electronics Brands
DELL = 'Dell'
HP = 'HP'
LENOVO = 'Lenovo'
ACER = 'Acer'
ASUS = 'Asus'
EPSON = 'Epson'
MEDITECH = 'MediTech'
SAMSUNG = 'Samsung'
X_TIG = 'X_Tig'
FUJITSU = 'Fujitsu'
CLONE = 'Clone'
PC_PERIPHERALS = 'P.C Peripherals'
STONE_PC = 'Stone PC'
SYSTEM_MANUFACTURER = 'System manufacturer'

BRAND_CHOICES = [
    (DELL, 'Dell'),
    (HP, 'HP'),
    (LENOVO, 'Lenovo'),
    (ACER, 'Acer'),
    (ASUS, 'Asus'),
    (EPSON, 'Epson'),
    (MEDITECH, 'MediTech'),
    (SAMSUNG, 'Samsung'),
    (X_TIG, 'X_Tig'),
    (FUJITSU, 'Fujitsu'),
    (CLONE, 'Clone'),
    (PC_PERIPHERALS, 'P.C Peripherals'),
    (STONE_PC, 'Stone PC'),
    (SYSTEM_MANUFACTURER, 'System manufacturer'),
]

# Devides status
NEW = 'New'
REFURBISHED = 'Refurbished'
USED = 'Used'

DEVICE_STATUS_CHOICES = [
    (REFURBISHED, 'Refurbished'),
    (NEW, 'New'),
    (USED, 'Used'),
]

# Processor Types
INTEL_I3 = 'intel i3'
INTEL_I5 = 'intel i5'
INTEL_I7 = 'intel i7'
DUAL_CORE = 'Dual Core'
PENTIUM_4 = 'Pentium 4'
QUAD_CORE = 'Quad Core'
AMD = 'AMD'

PROCESSOR_TYPE_CHOICES = [
    (INTEL_I3, 'intel i3'),
    (INTEL_I5, 'intel i5'),
    (INTEL_I7, 'intel i7'),
    (DUAL_CORE, 'Dual Core'),
    (PENTIUM_4, 'Pentium 4'),
    (QUAD_CORE, 'Quad Core'),
    (AMD, 'AMD'),
]

# RAM Types
DRAM = 'DRAM'
SRAM = 'SRAM'

RAM_TYPE_CHOICES = [
    (DRAM, 'DRAM'),
    (SRAM, 'SRAM'),
]

# RAM Sizes
FIVE12 = '512 MB'
ONE_GB = '1 GB'
TWO_GB = '2 GB'
FOUR_GB = '4 GB'
EGIHT_GB = '8 GB'

RAM_SIZE_CHOICES = [
    (FIVE12, '512 MB'),
    (ONE_GB, '1 GB'),
    (TWO_GB, '2 GB'),
    (FOUR_GB, '4 GB'),
    (EGIHT_GB, '8 GB'),
]

# Storage Types
SSD = 'SDD'
HDD = 'HDD'
ROM = 'ROM'
SD_CARD = 'SD Card'

STORAGE_TYPE_CHOICES = [
    (HDD, 'HDD'),
    (SSD, 'SSD'),
    (ROM, 'ROM'),
    (SD_CARD, 'SD Card'),
]

# Storage Sizes

GB80 = '80 GB'
GB128 = '128 GB'
GB160 = '160 GB'
GB250 = '250 GB'
GB320 = '320 GB'
GB500 = '500 GB'
TB1 = '1 TB'
GB16 = '16 GB'
GB32 = '32 GB'
GB8 = '8 GB'

STORAGE_SIZE_CHOICES = [
    (GB80, '80 GB'),
    (GB128, '128 GB'),
    (GB160, '160 GB'),
    (GB250, '250 GB'),
    (GB320, '320 GB'),
    (GB500, '500 GB'),
    (TB1, '1 TB'),
    (GB8, '8 GB'),
    (GB16, '16 GB'),
    (GB32, '32 GB'),
]

# OS Type Installed
MAC = 'Mac OS'
WINDOWS = 'Windows'
LINUX = 'Linux'
ANDROID = 'Android'
NO_OS = 'No OS'

OS_TYPE_CHOICES = [
    (LINUX, 'Linux'),
    (MAC, 'Mac OS'),
    (WINDOWS, 'Windows'),
    (ANDROID, 'Android'),
    (NO_OS, 'No OS'),
]

# Computer and Monitor Status
WORKING = 'Working'
PROBLEMATIC = 'Problematic'
DESPATCHED = 'Dispatched'
PROCESSED = 'Processed'
EWASTE = 'E-Waste'
NOT_RECEIVED = 'Not Received'

COMPUTER_STATUS_CHOICES = [
    (WORKING, 'Working'),
    (PROCESSED, 'Processed'),
    (PROBLEMATIC, 'Problematic'),
    (EWASTE, 'E-Waste'),
    (NOT_RECEIVED, 'Not Received'),
]

MONITOR_STATUS_CHOICES = [
    (PROCESSED, 'Processed'),
    (PROBLEMATIC, 'Problematic'),
    (EWASTE, 'E-Waste'),
    (NOT_RECEIVED, 'Not Received'),
]
# Device type choices
SYSTEM_UNIT = 'System Unit'
TABLET = 'Tablet'
LAPTOP = 'Laptop'
PRINTER = 'Printer'
PROJECTOR = 'Projector'

DEVICE_TYPE_CHOICES = [
    (SYSTEM_UNIT, 'System Unit'),
    (TABLET, 'Tablet'),
    (LAPTOP, 'Laptop'),
    (PRINTER, 'Printer'),
    (PROJECTOR, 'Projector'),
]

# Screen Size
UNKNOWN = 'Unknown'
INCH17 = '17 inch'
INCH19 = '19 inch'
INCH21 = '21 inch'
INCH20 = '20 INCH'
INCH15 = '15 INCH'

SCREEN_SIZE_CHOICES = [
    (UNKNOWN, 'Unknown'),
    (INCH15, '15 inch'),
    (INCH17, '17 inch'),
    (INCH19, '19 inch'),
    (INCH20, '20 inch'),
    (INCH21, '21 inch'),
]

#Payment Methods

CASH = 'Cash'
CHEQUIE = 'Chequie'
BANK_TRANSFER = 'Bank Transfer'

PAYMENT_METHOD = [
    (CASH, 'Cash'),
    (CHEQUIE, 'Chequie'),
    (BANK_TRANSFER, 'Bank Transfer'),
]

# Supplier Category

LOCAL = 'Local'
INTERNATIONAL = 'International'

SUPPLIER_CATEGORY = [
    (LOCAL, 'Local'),
    (INTERNATIONAL, 'International'),
]