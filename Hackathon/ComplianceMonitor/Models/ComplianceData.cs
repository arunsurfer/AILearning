using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ComplianceMonitor.Models
{
    public class ComplianceData
    {
        public List<Regulation> Regulations { get; set; }

    }

    public class ComplianceSummary
    {
        public string ChunkTitle { get; set; }
        public string Brief { get; set; }
        public DateTime? FollowUpDate { get; set; }
    }
}
