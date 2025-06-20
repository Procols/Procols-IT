// Optional JS for enhanced dropdown interaction (like click to toggle)
document.addEventListener('DOMContentLoaded', () => {
    const dropdown = document.querySelector('.dropdown');
    dropdown.addEventListener('click', (e) => {
      e.stopPropagation();
      const content = dropdown.querySelector('.dropdown-content');
      content.style.display = content.style.display === 'grid' ? 'none' : 'grid';
    });
  
    document.addEventListener('click', () => {
      const content = document.querySelector('.dropdown-content');
      if (content) content.style.display = 'none';
    });
  });
  