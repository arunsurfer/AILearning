using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ComplianceMonitor.Models
{
    public class Subsection
    {
        public string Title { get; set; }
        public string Content { get; set; }
    }

    public class Regulation
    {
        public string Section { get; set; }
        public List<Subsection> Subsections { get; set; }
    }
}
