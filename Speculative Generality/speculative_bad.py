"""
Sales Report Exporter
----------------------
Exports a sales summary report.

YOUR TASK: This script works correctly, but it's over-engineered for
requirements that don't exist yet — flexibility "just in case" that's
never actually used. Find it and strip it back to what's really needed.
Do NOT change the printed output.

Hint: look for unused constructor parameters, methods that set state
nobody reads, an abstraction built for only one real implementation, and
config options that only ever have one real value.
"""

sales_data = [
    {"product": "Widget A", "units": 120, "revenue": 2400.0},
    {"product": "Widget B", "units": 45, "revenue": 1350.0},
    {"product": "Widget C", "units": 200, "revenue": 3000.0},
]


class ReportExporter:
    def __init__(
        self,
        export_format="text"
    ):
        self.export_format = export_format
        
    def export(self, data, title):
        if self.export_format != "text":
            raise NotImplementedError("Only text export is currently supported")

        lines = [f"=== {title} ==="]
        total_units = 0
        total_revenue = 0.0

        for row in data:
            lines.append(
                f"{row['product']}: {row['units']} units, ${row['revenue']:.2f}"
            )
            total_units += row["units"]
            total_revenue += row["revenue"]

        lines.append(f"Total units sold: {total_units}")
        lines.append(f"Total revenue: ${total_revenue:.2f}")

        return "\n".join(lines)


def generate_report(data, report_type="standard"):
    if report_type != "standard":
        raise NotImplementedError("Only 'standard' report type exists right now")

    exporter = ReportExporter()
    return exporter.export(data, "Q1 Sales Summary")
  


if __name__ == "__main__":
    report = generate_report(sales_data)
    print(report)