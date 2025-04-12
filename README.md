# Django Multiple Users Application

## Overview
This Django application manages materials and compounds with user-specific views and forms. It includes features like listing materials, listing compounds, and creating new compounds using forms.

---

## Features
- **Materials Management**:
  - List all materials using `MaterialsListView`.
- **Compounds Management**:
  - List all compounds using `CompListView`.
  - Add new compounds using a form (`createcompound` view).
- **Class-Based Views**:
  - Utilizes Django's `ListView` for efficient data rendering.
- **Form Handling**:
  - Handles form submissions for creating new compounds.

---

## Views

### 1. **Materials List View**
The `MaterialsListView` displays a list of all materials.

#### Code:
```python
class MaterialsListView(ListView):
    model = Material

    def get(self, request, *args, **kwargs):
        objects = Material.objects.all()
        context = {"materials": objects}
        return render(request, "Materials-list.html", context)
```

#### Template:
- **Template Name**: `Materials-list.html`
- **Context**: `materials` (list of all `Material` objects)

---

### 2. **Compounds List View**
The `CompListView` displays a list of all compounds.

#### Code:
```python
class CompListView(ListView):
    model = compound
    queryset = compound.objects.all()

    def get(self, request, *args, **kwargs):
        objects = compound.objects.all()
        context = {"object_list": objects}
        return render(request, "compound-list.html", context)
```

#### Template:
- **Template Name**: `compound-list.html`
- **Context**: `object_list` (list of all `compound` objects)

---

### 3. **Create Compound View**
The `createcompound` view allows users to add new compounds using a form.

#### Code:
```python
def createcompound(request):
    form = compoundForm()
    if request.method == 'POST':
        form = compoundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'add-compound.html', context)
```

#### Template:
- **Template Name**: `add-compound.html`
- **Context**: `form` (instance of `compoundForm`)

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/django-multiple-users.git
cd django-multiple-users
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Run migrations to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Visit the application at `http://127.0.0.1:8000`.

---

## Project Structure
```
django_multiple_users/
├── materials/
│   ├── models.py        # Models for Material and compound
│   ├── views.py         # Views for listing and creating compounds
│   ├── templates/       # HTML templates for materials and compounds
│   ├── forms.py         # Form for creating compounds
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

---

## Dependencies
- **Django**: Backend framework
- **Python**: Programming language
- **SQLite**: Default database for development

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

