
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from datetime import datetime
import numpy as np
def create_first_page(student_name, device_used, assessment_date, drill_type, 
                     test_duration, assessed_by,story,styles):

    # Header with Logo and Company Name
    header_data = [[
        Image('hyperlab_logo.png', width=1.2*inch, height=0.5*inch),
        Paragraph(
            "<font color='#2E4053' size='16'><b>Hyperlab Sportech Pvt. Ltd. </b></font><br/>"
            "<font color='#5D6D7E' size='10'>Advanced Performance Assessment</font>",
            styles['Normal']
        )
    ]]
    header_table = Table(header_data, colWidths=[1.5*inch, 5.5*inch])
    header_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (1, 0), (1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(header_table)
    
    # Decorative Line
    line_table = Table([['']], colWidths=[7.5*inch], rowHeights=[2])
    line_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ('LINEBELOW', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053'))
    ]))
    story.append(line_table)
    
    story.append(Spacer(1, 20))
    
    # Title Style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=12,
        textColor=colors.HexColor('#2E4053')
    )
    
    intro_paragraph_style = ParagraphStyle(
        'IntroParagraph',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        spaceBefore=6,
        spaceAfter=8,
        alignment=TA_JUSTIFY
    )

    # Title
    story.append(Paragraph("Concentration Drill Assessment Report", title_style))
    
    # Information table with branded styling
    info_data = [
        ["Student Name:", student_name, "Date of Assessment:", assessment_date],
        ["Device Used:", device_used, "Drill Type:", drill_type],
        ["Test Duration:", test_duration, "Assessed by:", assessed_by]
    ]
    
    info_table = Table(info_data, colWidths=[1.5*inch, 2*inch, 1.5*inch, 2*inch])
    info_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F4F6F7')),
        ('BACKGROUND', (2, 0), (2, -1), colors.HexColor('#F4F6F7')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 20))

    # Introduction Section
    story.append(Paragraph("Introduction", section_title_style))
    
    intro_text = """The <b>Concentration Drill</b>, developed by HyperLab Technologies, is an advanced cognitive assessment tool designed to evaluate three critical mental capabilities: <b>attention</b>, <b>reaction speed</b>, and <b>inhibitory control</b>. Using our proprietary HELIOS technology, this drill creates a standardized testing environment that challenges participants through unpredictable auditory cues (single and double beeps) while measuring their ability to maintain focus and control under progressive time pressure."""
    story.append(Paragraph(intro_text, intro_paragraph_style))
    
    story.append(Spacer(1, 1))
    
    intro_text2 = """The purpose of this assessment is to provide detailed insights into a participant's cognitive functioning, specifically measuring their ability to: maintain sustained attention, respond quickly to relevant stimuli, and suppress inappropriate responses. These abilities are fundamental to both academic performance and athletic excellence, making this assessment valuable for identifying areas of strength and potential improvement."""
    story.append(Paragraph(intro_text2, intro_paragraph_style))
    
    story.append(Spacer(1, 15))

    # Procedure Section with branded header
    procedure_header = Table(
        [[Paragraph("Drill Structure and Procedure", section_title_style)]],
        colWidths=[7.5*inch],
        rowHeights=[40]
    )
    procedure_header.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(procedure_header)
    story.append(Spacer(1, 10))
    
    procedure_data = [
    ["Stage", "Description", "Details"],
    ["1. Initialization", 
     "System calibration\nParticipant positioning",
     "• Initial sweep (±40°) for system check\n• Participant confirming readiness with tap"],
    ["2. Target Distribution", 
     "50 total assessment points\nBalanced evaluation",
     "• 10 points per level, max 5 levels\n• Distance range: 700-1000mm\n• Angular range: -40° to +40°"],
    ["3. Response Types", 
     "Two distinct response patterns\nProgressive difficulty",
     "• Single beep: Requires tap response\n• Double beep: Requires no action\n• Drill ends after 2 misses in any level"],
    ["4. Target Presentation", 
     "Randomized positioning\nVariable timing",
     "• Random target positions each trial\n• Decreasing response window per level\n• Level 1: 700ms → Level 5: 300ms"],
    ["5. Performance Tracking", 
     "Real-time monitoring\nPrecise measurement",
     "• Success: Move to next target\n• Error: Head shake feedback\n• Response time tracking"],
    ["6. Scoring System", 
     "Three-tier evaluation\nComprehensive feedback",
     "• Hit (+1): Correct tap or no-tap\n• Miss (0): No tap when needed\n• Error (-1): Wrong tap timing\n• Early termination on 2 misses"]
    ]
    procedure_table = Table(procedure_data, colWidths=[1.65*inch, 2*inch,2.7*inch])
    procedure_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F4F6F7')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    
    story.append(procedure_table)
    
    # Footer with branding
    # story.append(Spacer(1, 20))
    # story=add_footer(story,styles)

    return story
    # Build the PDF
def calculate_metrics(results):
        # Basic counts
    total_points = len(results)
    correct_taps = results.count(1)
    correct_non_taps = results.count(0)
    incorrect_responses = results.count(-1)
    
    # Overall metrics
    accuracy = ((correct_taps + correct_non_taps) / total_points) * 100
    inhibitory_control = (correct_non_taps / 25) * 100  # Assuming 25 double beep points
    
    overall_score = (correct_taps / total_points) * 10
    
    
    # Segment analysis
    segments = [results[i:i+10] for i in range(0, len(results), 10)]
    segment_metrics = []
    
    for i, segment in enumerate(segments):
        seg_correct_taps = segment.count(1)
        seg_correct_non_taps = segment.count(0)
        seg_incorrect = segment.count(-1)
        
        segment_metrics.append({
            'segment': i + 1,
            'accuracy': ((seg_correct_taps + seg_correct_non_taps) / 10) * 100,
            'tap_rate': (seg_correct_taps / (10 if i != len(segments)-1 else len(segment))) * 100,
            'non_tap_rate': (seg_correct_non_taps / (10 if i != len(segments)-1 else len(segment))) * 100,
            'error_rate': (seg_incorrect / (10 if i != len(segments)-1 else len(segment))) * 100
        })
    
    # Calculate consistency metrics
    accuracies = [m['accuracy'] for m in segment_metrics]
    tap_rates = [m['tap_rate'] for m in segment_metrics]
    consistency_score = 100 - np.std(accuracies)  # Higher score means more consistent
    adaptability_score = (segment_metrics[-1]['accuracy'] / segment_metrics[0]['accuracy']) * 100
    
    return {
        'basic_metrics': {
            'correct_taps': correct_taps,
            'correct_non_taps': correct_non_taps,
            'incorrect_responses': incorrect_responses,
            'accuracy': accuracy,
            'inhibitory_control': inhibitory_control,
            'overall_score': overall_score
        },
        'segment_metrics': segment_metrics,
        'consistency_metrics': {
            'consistency_score': consistency_score,
            'adaptability_score': adaptability_score,
            'accuracy_std': np.std(accuracies),
            'tap_rate_std': np.std(tap_rates)
        }
    }

def create_performance_metrics_page(story, styles, results):
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    import numpy as np
    from datetime import datetime
    
    story.append(PageBreak())
    metrics = calculate_metrics(results)

    # Styles
    title_style = ParagraphStyle(
        'MetricsTitle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    section_style = ParagraphStyle(
        'MetricsSection',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor('#34495E')
    )
    
    # Page Title
    story.append(Paragraph("Detailed Performance Metrics", title_style))
    # Calculate all metrics

    level_data = get_assessment_level(metrics['basic_metrics']['overall_score'])
    
    # Create assessment box with score
    assessment_content = [
        [Paragraph(f"""
        <font color='{level_data['color']}' size='11'><b>{level_data['level']}</b></font>
        <br/>
        <font color="#7F8C8D" size='8'><b>Overall Score: {metrics['basic_metrics']['overall_score']:.1f}/10</b></font>
        <br/>
        <font color='#5D6D7E' size='9'>Assessment based on overall performance metrics</font>
        """, styles['Normal'])]
    ]
    
    assessment_box = Table(assessment_content, colWidths=[6*inch])
    assessment_box.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053')),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(assessment_box)
    story.append(Spacer(1, 20))
    
    
    # Primary Metrics Table
    story.append(Paragraph("Primary Performance Indicators", section_style))
    
    primary_data = [
        ["Metric", "Value", "Optimal Range"],
        ["Overall Accuracy", f"{metrics['basic_metrics']['accuracy']:.1f}%", "85-100%"],
        ["Inhibitory Control", f"{metrics['basic_metrics']['inhibitory_control']:.1f}%", "80-100%"],
        ["Consistency Score", f"{metrics['consistency_metrics']['consistency_score']:.1f}", "Above 85"],
        ["Adaptability Score", f"{metrics['consistency_metrics']['adaptability_score']:.1f}%", "Above 80%"],
        ["Overall Score", str(metrics['basic_metrics']['overall_score']), "8-10"]
    ]
    
    primary_table = Table(primary_data, colWidths=[2*inch, 2*inch, 2*inch])
    primary_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F8F9F9')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(primary_table)
    story.append(Spacer(1, 20))
    
    # Segmented Performance Analysis
    story.append(Paragraph("Performance Progression Analysis", section_style))
    
    segment_headers = ["Segment", "Accuracy", "Tap Rate", "Non-Tap Rate", "Error Rate"]
    segment_data = [segment_headers]
    
    timeout_times = [1000, 800, 600, 400, 200]  # Example timeout times in ms
    
    for i, segment in enumerate(metrics['segment_metrics']):
        segment_data.append([
            f"Segment {i+1}\n({timeout_times[i]}ms)",
            f"{segment['accuracy']:.1f}%",
            f"{segment['tap_rate']:.1f}%",
            f"{segment['non_tap_rate']:.1f}%",
            f"{segment['error_rate']:.1f}%"
        ])
    
    segment_table = Table(segment_data, colWidths=[1.2*inch, 1.2*inch, 1.2*inch, 1.2*inch, 1.2*inch])
    segment_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F8F9F9')),
    ]))
    
    story.append(segment_table)
    story.append(Spacer(1, 8))

    # Add parameter explanations as a simple note
    note_style = ParagraphStyle(
        'Note',
        parent=styles['Normal'],
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#666666'),
    )

    parameter_note = """
    <i>Note: Accuracy - Overall success rate per segment | Tap Rate - Success in responding to single beeps | 
    Non-Tap Rate - Success in inhibiting response to double beeps | Error Rate - Percentage of incorrect or missed responses</i>
    """

    story.append(Paragraph(parameter_note, note_style))
    story.append(Spacer(1, 10))
    # Response Distribution
    story.append(Paragraph("Response Distribution Analysis", section_style))
    
    distribution_data = [
        ["Response Type", "Count", "Percentage", "Optimal Value"],
        ["Correct Taps", 
         str(metrics['basic_metrics']['correct_taps']),
         f"{(metrics['basic_metrics']['correct_taps']/50)*100:.1f}%",
         "25"],
        ["Correct Non-Taps",
         str(metrics['basic_metrics']['correct_non_taps']),
         f"{(metrics['basic_metrics']['correct_non_taps']/50)*100:.1f}%",
         "25"],
        ["Incorrect/Missed",
         str(metrics['basic_metrics']['incorrect_responses']),
         f"{(metrics['basic_metrics']['incorrect_responses']/50)*100:.1f}%",
         "0"]
    ]
    
    distribution_table = Table(distribution_data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
    distribution_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F8F9F9')),
        ('TEXTCOLOR', (-1, -1), (-1, -1), colors.HexColor('#E74C3C')),
        ('TEXTCOLOR', (-1, -2), (-1, -3), colors.HexColor('#27AE60')),
    ]))
    
    story.append(distribution_table)
    
    story.append(Spacer(1, 15))
    story.append(Paragraph("Quick Performance Interpretation", section_style))
    
    # Generate interpretations based on metrics
    def generate_interpretations(metrics):
        interpretations = []
        
        # Accuracy Interpretation
        accuracy = metrics['basic_metrics']['accuracy']
        if accuracy >= 85:
            interpretations.append("Superior accuracy indicating excellent attention control")
        elif accuracy >= 70:
            interpretations.append("Good accuracy with room for improvement in attention control")
        else:
            interpretations.append("Attention control needs focused development")
            
        # Inhibitory Control Interpretation
        inhib = metrics['basic_metrics']['inhibitory_control']
        if inhib >= 80:
            interpretations.append("Strong inhibitory control showing good response suppression")
        else:
            interpretations.append("Inhibitory control requires additional practice")
            
        # Consistency Interpretation
        if metrics['consistency_metrics']['consistency_score'] >= 85:
            interpretations.append("Highly consistent performance across all segments")

        elif 85>metrics['consistency_metrics']['consistency_score']>=70:
            interpretations.append("Performance consistency varies moderately across segments")
        else:
            interpretations.append("Performance consistency varies drastically across segments")
        
        return interpretations
              
    interpretations = generate_interpretations(metrics)
    
    # Create interpretation table
    interp_data = [[Paragraph(f"• {interp}", styles['Normal'])] for interp in interpretations]
    interp_table = Table(interp_data, colWidths=[6*inch])
    interp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
    ]))
    
    story.append(interp_table)
    
    # Add Overall Performance Level indica
    # Footer remains the same
    # story.append(Spacer(1, 20))
    # story=add_footer(story,styles)
    return story

def add_footer(story,styles):
    # return story
    footer_text = f"Generated on {datetime.now().strftime('%B %d, %Y')} | Confidential Assessment Report | Page 2 | ©2024 HyperLab"
    footer_text_style = ParagraphStyle(
        'FooterText',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.gray,  # This sets the text color to gray
    )

    footer_data = [[
        Image('hyperlab_logo_small.png', width=0.5*inch, height=0.2*inch),
        Paragraph(
            f"Generated on {datetime.now().strftime('%B %d, %Y')} | Confidential Assessment Report | Page 1 | ©2024 HyperLab",
            footer_text_style  # Use the new style here instead of styles['Normal']
        )
    ]]

    footer_table = Table(footer_data, colWidths=[0.7*inch, 6.8*inch])
    footer_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
    ]))
    story.append(footer_table)
    return story


def create_final_branding_page(story, styles):
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    from reportlab.platypus import Spacer, Table, TableStyle, Image
    story.append(PageBreak())
    story.append(Spacer(1, 2*inch))
    
    # Large centered logo
    logo_table = Table([[Image('hyperlab_logo.png', width=3*inch, height=1.2*inch)]], 
                      colWidths=[7.5*inch])
    logo_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(logo_table)
    
    story.append(Spacer(1, inch))
    
    # Company information
    info_style = ParagraphStyle(
        'CompanyInfo',
        parent=styles['Normal'],
        fontSize=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053'),
        spaceAfter=12
    )
    
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#5D6D7E'),
        spaceAfter=8
    )
    
    info_data = [
        [Paragraph("<b>HyperLab Sportech Pvt. Ltd.</b>", info_style)],
        [Paragraph("Advanced Performance Assessment & Training Solutions", contact_style)],
        [Paragraph("https://www.hyperlab.life/ | contact@hyperlab.life", contact_style)],
        [Paragraph("support@hyperlab.life", contact_style)],
    ]
    
    info_table = Table(info_data, colWidths=[7.5*inch])
    info_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(info_table)
    
    story.append(Spacer(1, 2*inch))
    
    # Bottom decorative element
    footer_text = "Excellence in Sports Science & Technology"
    footer_style = ParagraphStyle(
        'BrandingFooter',
        parent=styles['Normal'],
        fontSize=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    story.append(Paragraph(footer_text, footer_style))
    
    # Add decorative line
    line_table = Table([['']], colWidths=[5*inch], rowHeights=[1])
    line_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ('LINEBELOW', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053'))
    ]))
    story.append(line_table)
    
    return story
def create_conc_report(student_name, device_used, assessment_date, drill_type, 
                     test_duration, assessed_by,results):
    doc = SimpleDocTemplate(
        f"concentration_drill_report_{student_name.lower().replace(' ', '_')}.pdf",
        pagesize=A4,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    # Create template with footer
    # create_report_template(doc)
    
    story = []
    styles = getSampleStyleSheet()
    story=create_first_page(student_name, device_used, assessment_date, drill_type, 
                     test_duration, assessed_by,story,styles)

    story=create_performance_metrics_page(story,styles,results)
    story=create_understanding_scores_page(story,styles,results)
    story=create_recommendations_page(story,styles,results)
    story=create_conclusion_page(story,styles,results)
    story = create_final_branding_page(story, styles)

    doc.build(story)
    return f"concentration_drill_report_{student_name.lower().replace(' ', '_')}.pdf"
    
def get_assessment_level(score):
    if score >= 8.5:
        return {
            'level': 'Excellent',
            'color': '#27AE60',
            'percentage': score * 10
        }
    elif score >= 7:
        return {
            'level': 'Good',
            'color': '#F39C12',
            'percentage': score * 10
        }
    elif score >= 5:
        return {
            'level': 'Fair',
            'color': '#E67E22',
            'percentage': score * 10
        }
    else:
        return {
            'level': 'Devloping',
            'color': '#E74C3C',
            'percentage': score * 10
        }
def create_understanding_scores_page(story, styles, results):
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    from datetime import datetime
    
    # Title Style
    story.append(PageBreak())
    metrics=calculate_metrics(results)
    title_style = ParagraphStyle(
        'UnderstandingTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    # Section Style
    section_style = ParagraphStyle(
        'MetricSection',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor('#34495E')
    )
    
    # Metric name style
    metric_name_style = ParagraphStyle(
        'MetricName',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#2E4053'),
        fontName='Helvetica-Bold'
    )
    
    # Description style
    description_style = ParagraphStyle(
        'MetricDescription',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#2E4053')
    )
    
    # Page Title
    story.append(Paragraph("Understanding Your Scores", title_style))
    story.append(Spacer(1, 20))
    
    # Introduction text
    intro_text = """This section provides a detailed explanation of each metric used in your assessment. Understanding these metrics will help you interpret your performance and identify areas for improvement. Each metric has been carefully designed to measure specific aspects of your cognitive performance during the Concentration Drill."""
    
    story.append(Paragraph(intro_text, description_style))
    story.append(Spacer(1, 20))

    
    
    # Primary Metrics Section
    metrics_data = [
        {
            "title": "Overall Accuracy",
            "description": """Measures the percentage of correct responses across all 50 points.This includes both \ncorrect taps for single beeps and correct non-taps for double beeps.""",
            "calculation": "Accuracy = ((Correct Taps + Correct Non-Taps) / Total Points) × 100",
            "interpretation": {
                "Excellent": "≥85%: Superior attention control",
                "Good": "70-84%: Effective performance",
                "Developing": "<70%: Needs improvement"
            },
            "your_score": f"{metrics['basic_metrics']['accuracy']:.1f}%"
        },
        {
            "title": "Inhibitory Control",
            "description": """Evaluates your ability to suppress automatic responses by measuring the accuracy of\nyour non-tap responses to double beeps.""",
            "calculation": "Inhibitory Control = (Correct Non-Taps / Total Double Beep Points) × 100",
            "interpretation": {
                "Strong": "≥80%: Excellent response suppression",
                "Moderate": "60-79%: Good control",
                "Developing": "<60%: Needs practice"
            },
            "your_score": f"{metrics['basic_metrics']['inhibitory_control']:.1f}%"
        },
        {
            "title": "Consistency Score",
            "description": """Measures how stable your performance remains across all segments of the drill,\naccounting for increasing time pressure.""",
            "calculation": "100 - Standard Deviation of Segment Accuracies",
            "interpretation": {
                "High": "≥85: Very consistent performance",
                "Moderate": "70-84: Some variability",
                "Variable": "<70: Significant fluctuation"
            },
            "your_score": f"{metrics['consistency_metrics']['consistency_score']:.1f}"
        },
        {
            "title": "Adaptability Score",
            "description": """Shows how well you maintain performance as the timeout duration decreases,indicating\nadaptation to time pressure.""",
            "calculation": "(Final Segment Accuracy / First Segment Accuracy) × 100",
            "interpretation": {
                "Excellent": "≥80%: Strong adaptation",
                "Good": "60-79%: Moderate adaptation",
                "Developing": "<60%: Needs improvement"
            },
            "your_score": f"{metrics['consistency_metrics']['adaptability_score']:.1f}%"
        },
        {
            "title": "Overall Score",
            "description": """A concentration score out of 10 that reflects your ability to maintain focus and respond\naccurately throughout the assessment.""",
            "calculation": "(Correct Taps / Total Points) × 10",
            "interpretation": {
                "Excellent": "≥8.5: Excellent concentration level",
                "Good": "7.0-8.4: Strong concentration ability",
                "Fair": "5.0-6.9: Moderate concentration",
                "Developing": "<5.0: Basic concentration level"
            },
            "your_score": f"{metrics['basic_metrics']['overall_score']:.1f}/10"
        }
    ]
    i=0
    for metric in metrics_data:
        # Metric Header
        if i==4:
            story.append(PageBreak())
        header_table = Table(
            [[Paragraph(metric["title"], metric_name_style)]],
            colWidths=[7*inch],
            rowHeights=[30]
        )
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(header_table)
        
        # Create content table
        content_data = [
            ["Description:", metric["description"]],
            ["Calculation:", metric["calculation"]],
            ["Your Score:", metric["your_score"]],
            ["Interpretation:", "\n".join([f"{k}: {v}" for k, v in metric["interpretation"].items()])]
        ]
        
        content_table = Table(content_data, colWidths=[1.5*inch, 5.5*inch])
        content_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F8F9F9')),
        ]))
        
        story.append(content_table)
        story.append(Spacer(1, 15))
        i+=1
    
    # Additional Information Section
    story.append(Paragraph("Additional Notes", section_style))
    
    notes_text = """
    • Scores are calculated based on responses to both single beep (tap required) and double beep (no tap required) points.
    • Time pressure increases every 10 points, requiring progressively faster responses.
    • The assessment evaluates both speed and accuracy, with emphasis on maintaining consistent performance.
    • Negative points for incorrect responses help identify areas needing focused practice.
    """
    
    notes_table = Table([[Paragraph(notes_text, description_style)]], colWidths=[7*inch])
    notes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('PADDING', (0, 0), (-1, -1), 12),
    ]))
    
    story.append(notes_table)
    
    # Footer
    
    return story
# Example usage

def create_recommendations_page(story, styles, results):
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    from datetime import datetime
    story.append(PageBreak())
    metrics=calculate_metrics(results)
    def get_specific_recommendations(metrics):
        recommendations = []
        # Accuracy-based recommendations
        accuracy = metrics['basic_metrics']['accuracy']
        if accuracy >= 85:
            recommendations.append({
                "focus_area": "Accuracy Mastery",
                "current_status": f"{accuracy:.1f}% accuracy(Excellent)",
                "target":  "Maintain >85% while increasing speed",
                "specific_exercises": [
                    "Stroop Test Practice: Use online Stroop test apps for 10-minute sessions (improves focused attention)",
                    "Schulte Table Training: Practice with 5x5 grid number finding exercises (builds visual scanning)",
                    "CogniFit Memory Matrix: Complete memory grid patterns with increasing complexity",
                    "Lumosity Speed Match: Practice quick pattern matching exercises"
                ],
                "practice_schedule": "2-3 sessions/week, 15-20 minutes per session",
                "progression_metrics": "Track completion time and accuracy percentage in each app",
                "colour":'#27AE60'

            })
        else:
            recommendations.append({
                "focus_area": "Response Accuracy Enhancement",
                "current_status": f"{accuracy:.1f}% accuracy",
                "target": ">85% accuracy",
                "specific_exercises": [
                    "Simple Reaction Time Test: Use online reaction time testers for 10 sets of 10 attempts",
                    "Number Memory Game: Practice with online digit span tests (start with 5 digits)",
                    "Pattern Memory Games: Use apps like Simon Says or Pattern Memory",
                    "Concentration Grid: Practice with 10x10 number grid exercises"
                ],
                "practice_schedule": "3-4 sessions/week, 15 minutes per session",
                "progression_metrics": "Record scores from each app/game and aim for consistent improvement",
                "colour":'#E3242B'

            })

        # Inhibitory control recommendations
        inhib_control = metrics['basic_metrics']['inhibitory_control']
        if inhib_control >= 80:
            recommendations.append({
                "focus_area": "Advanced Inhibitory Control",
                "current_status": f"{inhib_control:.1f}% inhibitory control(Strong)",
                "target": "Maintain excellence while\nincreasing complexity",
                "specific_exercises": [
                    "Advanced Go/No-Go Games: Use online Go/No-Go test apps at maximum difficulty",
                    "Dual N-Back Training: Practice with free Dual N-Back apps (start at 2-back)",
                    "Color Word Match Games: Use advanced Stroop test variations",
                    "Response Inhibition Apps: Games like 'Stop Signal' or 'Red Light, Green Light'"
                ],
                "practice_schedule": "2-3 sessions/week, 20 minutes per session",
                "progression_metrics": "Track error rates and response times in each exercise",
                "colour":'#27AE60'

            })
        else:
            recommendations.append({
                "focus_area": "Inhibitory Control Development",
                "current_status": f"{inhib_control:.1f}% inhibitory control:",
                "target": ">90% successful inhibition",
                "specific_exercises": [
                    "Basic Go/No-Go Games: Start with simple online Go/No-Go tests",
                    "Stop Signal Games: Use free stop signal reaction time tests",
                    "Simple Stroop Test: Practice basic color-word matching exercises",
                    "Pattern Break Games: Use pattern sequence games with occasional breaks"
                ],
                "practice_schedule": "4 sessions/week, 15 minutes per session",
                "progression_metrics": "Keep score log for each game, aim for 90% accuracy before increasing speed",
                "colour":'#E3242B'

            })

        # Adaptability Score recommendations
        adaptability = metrics['consistency_metrics']['adaptability_score']
        if adaptability >= 80:
            recommendations.append({
                "focus_area": "Excellent Adaptability Training",
                "current_status": f"{adaptability:.1f}% (Excellent)",
                "target": "Maintain Excellent performance\nunder maximum time pressure",
                "specific_exercises": [
                    "BrainHQ Double Decision: Practice with increasing speeds (available online)",
                    "Quick Math Games: Use math reaction games with decreasing time limits",
                    "Lumosity Speed Pack Games: Focus on games that adjust difficulty automatically",
                    "Human Benchmark Tests: Practice full test suite with decreasing time limits"
                ],
                "practice_schedule": "2-3 sessions/week, varying games each session",
                "progression_metrics": "Record scores and completion times for each game type",
                "colour":'#27AE60'

            })
        elif adaptability >= 70:
            recommendations.append({
                "focus_area": "Advanced Adaptability Development",
                "current_status": f"{adaptability:.1f}% (Good)",
                "target": ">85% adaptability under increasing\ntime pressure",
                "specific_exercises": [
                    "Reaction Time Training: Use online reaction time tests with varying intervals",
                    "Pattern Speed Match: Practice with online pattern matching games at increasing speeds",
                    "Attention Switch Games: Games requiring rapid task switching",
                    "Memory Match Speed Games: Card matching games with decreasing time limits"
                ],
                "practice_schedule": "3 sessions/week, 20 minutes per session",
                "progression_metrics": "Track scores as game speed increases",
                "colour":'orange'

            })
        else:
            recommendations.append({
                "focus_area": "Foundational Adaptability Building",
                "current_status": f"{adaptability:.1f}% adaptability",
                "target": ">80% adaptability score",
                "specific_exercises": [
                    "Basic Reaction Games: Start with simple online reaction time tests",
                    "Speed Cards: Online card matching games at comfortable speeds",
                    "Simple Pattern Match: Basic pattern recognition games",
                    "Beginner Level Brain Training Apps: Start with Lumosity or Peak basic exercises"
                ],
                "practice_schedule": "4 sessions/week, 15 minutes per session",
                "progression_metrics": "Record baseline scores and track improvements",
                "colour":'#E3242B'

            })
        return recommendations
    
    # Title Style
    title_style = ParagraphStyle(
        'RecommendationsTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    # Section Style
    section_style = ParagraphStyle(
        'RecSection',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor('#34495E')
    )
    
    # Page Title
    story.append(Paragraph("Personalized Training Recommendations", title_style))
    
    # Introduction
    intro_style = ParagraphStyle(
        'Introduction',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#2E4053')
    )
    
    intro_text = f"""Based on your performance metrics, we have designed a personalized training program targeting specific areas for improvement. 
    Each recommendation includes detailed exercises, clear progression metrics, and a structured practice schedule to help you achieve optimal performance."""
    
    story.append(Paragraph(intro_text, intro_style))
    story.append(Spacer(1, 20))
    
    # Get personalized recommendations
    recommendations = get_specific_recommendations(metrics)
    
    # Create recommendation sections
    for i, rec in enumerate(recommendations):
        # Focus Area Header with Icon
        # header_bg_color = [colors.HexColor('#27AE60'), colors.HexColor('#2980B9'), colors.HexColor('#8E44AD')][i % 3]
        header_bg_color =rec['colour']
        
        
        header_table = Table(
            [[Paragraph(rec["focus_area"], 
                    ParagraphStyle('FocusArea',
                                    parent=styles['Normal'],
                                    fontSize=14,
                                    textColor=colors.white,
                                    fontName='Helvetica-Bold',
                                    leading=16,  # Added leading for better vertical spacing
                                    spaceAfter=6))]],  # Added space after paragraph
            colWidths=[7*inch],
            rowHeights=25  # Fixed height for header box
        )
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), header_bg_color),
            ('PADDING', (0, 0), (-1, -1), 8),  # Adjusted padding
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Added vertical alignment
            ('LEFTPADDING', (0, 0), (-1, -1), 12),  # Specific left padding
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),  # Specific right padding
            ('TOPPADDING', (0, 0), (-1, -1), 6),    # Specific top padding
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Specific bottom padding
        ]))
        story.append(header_table)
        
        # Status and Target
        status_data = [
            ["Current Status:", rec["current_status"], "Target:", rec["target"]]
        ]
        
        status_table = Table(status_data, colWidths=[1.25*inch, 2.25*inch, 1.25*inch, 2.25*inch])
        status_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F4F6F7')),
            ('BACKGROUND', (2, 0), (2, -1), colors.HexColor('#F4F6F7')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ]))
        story.append(status_table)
        
        # Specific Exercises
        exercise_data = [["Recommended Exercises:"]]
        for ex in rec["specific_exercises"]:
            exercise_data.append([f"• {ex}"])
            
        exercise_table = Table(exercise_data, colWidths=[7*inch])
        exercise_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#F4F6F7')),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ]))
        story.append(exercise_table)
        
        # Practice Schedule and Progression
        schedule_data = [
            ["Practice Schedule:", rec["practice_schedule"]],
            ["Progression Metrics:", rec["progression_metrics"]]
        ]
        
        schedule_table = Table(schedule_data, colWidths=[1.5*inch, 5.5*inch])
        schedule_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F4F6F7')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ]))
        story.append(schedule_table)
        story.append(Spacer(1, 20))
    
    # Additional Notes
    notes_style = ParagraphStyle(
        'Notes',
        parent=styles['Normal'],
        fontSize=10,
        leading=12,
        textColor=colors.HexColor('#2E4053')
    )
    
    notes_text = """
    <b>Important Notes:</b>
    • All the given exercises are easily available on web
    • Start each training session with a 2-minute warm-up exercise
    • Take 30-second breaks between exercise sets
    • Monitor fatigue levels and adjust intensity as needed
    • Record your progress after each session
    • Reassess performance every 2 weeks
    """
    
    notes_table = Table([[Paragraph(notes_text, notes_style)]], colWidths=[7*inch])
    notes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('PADDING', (0, 0), (-1, -1), 12),
    ]))
    
    story.append(notes_table)
    
    # Footer
    # story.append(Spacer(1, 60))
    # story=add_footer(story,styles)
    return story

def create_conclusion_page(story, styles, results):
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    from datetime import datetime
    story.append(PageBreak())
    metrics=calculate_metrics(results)
    def get_performance_summary(metrics):
        # Calculate overall performance level
        accuracy = metrics['basic_metrics']['accuracy']
        inhib_control = metrics['basic_metrics']['inhibitory_control']
        adaptability = metrics['consistency_metrics']['adaptability_score']
        overall_score = metrics['basic_metrics']['overall_score']
        
        if overall_score >= 45:
            level = "Excellent"
            potential = "exceptional potential for high-performance athletics"
        elif overall_score >= 35:
            level = "advanced"
            potential = "strong foundation for athletic excellence"
        elif overall_score>=25:
            level = "moderate"
            potential = "solid basis for athletic development"
        else:
            level = "Devloping"
            potential = "Devloping for athletic development"
            
        return level, potential
    
    # Title Style
    title_style = ParagraphStyle(
        'ConclusionTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    # Create decorative top banner
    banner_table = Table([['Assesment Conclusion']], colWidths=[7.5*inch], rowHeights=[40])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 16),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 20))
    
    # Get performance summary
    level, potential = get_performance_summary(metrics)
    
    # Key Metrics Summary Box
    metrics_style = ParagraphStyle(
        'MetricsSummary',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    metrics_data = [
        [Paragraph(f"<b>Overall Score</b><br/>{metrics['basic_metrics']['overall_score']}", metrics_style),
         Paragraph(f"<b>Accuracy</b><br/>{metrics['basic_metrics']['accuracy']:.1f}%", metrics_style),
         Paragraph(f"<b>Inhibitory Control</b><br/>{metrics['basic_metrics']['inhibitory_control']:.1f}%", metrics_style),
         Paragraph(f"<b>Adaptability</b><br/>{metrics['consistency_metrics']['adaptability_score']:.1f}%", metrics_style)]
    ]
    
    metrics_table = Table(metrics_data, colWidths=[1.875*inch]*4)
    metrics_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8F9F9')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 15),
    ]))
    story.append(metrics_table)
    story.append(Spacer(1, 30))
    
    # Conclusion Text
    conclusion_style = ParagraphStyle(
        'Conclusion',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#2E4053')
    )
    
    conclusion_text = f"""Based on your concentration drill assessment, you have demonstrated a <b>{level}</b> level of cognitive performance, 
    indicating {potential}. Your results show particular strengths in maintaining focus under varying time pressures and adapting to changing response requirements.
    
    The comprehensive analysis of your performance provides valuable insights into your cognitive capabilities, which are crucial for athletic excellence. 
    By following the personalized recommendations provided in this report, you can further enhance these abilities and optimize your performance potential."""
    
    story.append(Paragraph(conclusion_text, conclusion_style))
    story.append(Spacer(1, 30))
    
    # Key Takeaways Box
    takeaways_header = Table(
        [["KEY TAKEAWAYS"]], 
        colWidths=[7.5*inch],
        rowHeights=[30]
    )
    takeaways_header.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#34495E')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
    ]))
    story.append(takeaways_header)
    
    takeaways_style = ParagraphStyle(
        'Takeaways',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#2E4053')
    )
    
    # Generate personalized takeaways based on metrics
    takeaways_text = f"""
    • Your accuracy level of {metrics['basic_metrics']['accuracy']:.1f}% shows {
    'excellent attention control' if metrics['basic_metrics']['accuracy'] >= 85 
    else 'good potential with room for improvement'}.
    
    • Inhibitory control at {metrics['basic_metrics']['inhibitory_control']:.1f}% indicates {
    'strong response management' if metrics['basic_metrics']['inhibitory_control'] >= 80 
    else 'an area for focused development'}.
    
    • Adaptability score of {metrics['consistency_metrics']['adaptability_score']:.1f}% demonstrates {
    'excellent adaptation to pressure' if metrics['consistency_metrics']['adaptability_score'] >= 80 
    else 'developing capacity for handling time pressure'}.
    """
    
    takeaways_table = Table(
        [[Paragraph(takeaways_text, takeaways_style)]],
        colWidths=[7.5*inch]
    )
    takeaways_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('PADDING', (0, 0), (-1, -1), 15),
    ]))
    story.append(takeaways_table)
    story.append(Spacer(1, 30))
    
    # End Note
    endnote_style = ParagraphStyle(
        'EndNote',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    endnote_text = """Remember, cognitive performance is a crucial component of athletic excellence. 
    Regular practice and focused training of these abilities will contribute significantly to your overall athletic development.
    
    <b>Best wishes for your journey to excellence with Hyperlab. Keep pushing your limits!</b>"""
    
    story.append(Paragraph(endnote_text, endnote_style))
    
    # Decorative bottom banner
    story.append(Spacer(1, 30))
    bottom_banner = Table([['']], colWidths=[7.5*inch], rowHeights=[3])
    bottom_banner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
    ]))
    story.append(bottom_banner)
    
    # # Footer
    # story.append(Spacer(1, 310))

    # story=add_footer(story,styles)
    return story

if __name__ == "__main__":
    report_file = create_conc_report(
        student_name="Alex Thompson",
        device_used="HELIOS Pro v2.0",
        assessment_date="October 25, 2024",
        drill_type="Concentration Assessment",
        test_duration="5 minutes",
        assessed_by="Dr. Sarah Johnson",
        results=[1]*25+[-1]*12+[0]*13

    )
    import os
    os.startfile(report_file)
    print(f"Report generated: {report_file}")